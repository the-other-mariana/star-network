
filename = 'RegistroPrueba_120422.psd'
file = open(filename,'rb')
mybyte = file.read(1)

s = ""
c = 0
p = 1

# CC2531EMK CLOCK
CLOCK = 32

NUM = 4
TS = 8
LEN = 2
STATUS = 2
# SPECIFIED IN PACKET SNIFFER > HELP > ABOUT PSD FILE FORMAT
SPARE = 136

starting = True
pckt_num = []
pckt_ts = []
pckt_len = []
pckt_payload = []
pckt_status = []
pckt_spare = []
N = 1

# 11 = 65, 9 = 60, 10 = 63 (LQI)

while mybyte:
    if c == 5: break
    # first byte: PACKET INFO
    if p == 1:
        s += "================\n"
        s += "PCKT INFO\n"
        binary_string = "{:08b}".format(int(mybyte.hex(), 16))
        inv = binary_string[::-1]
        used_bits = inv[:4]
        if used_bits[0] == '1':
            s += 'FCS: true '
        else:
            s += 'FCS: false '
        if used_bits[1] == '1':
            s += 'CORR: 1 '
        else:
            s += 'CORR: 0 '
        if used_bits[2] == '1':
            s += 'BUFF_OVERFLOW: true '
        else:
            s += 'BUFF_OVERFLOW: false '
        if used_bits[3] == '1':
            s += 'GENERIC: true '
        else:
            s += 'GENERIC: false '
        s += '\n'
        p+=1
        starting = False
        mybyte = file.read(1)
        pckt_num = []
        continue
    # next 4 bytes: PACKET NUMBER
    if p > 1 and p <= (1 + NUM): # 1 and 5
        pckt_num.append(mybyte)
        if p == (1 + NUM): # 5
            b = b''.join(pckt_num)
            value = int.from_bytes(b, byteorder='little')
            s += f"PCKT NUM({NUM}): {pckt_num} = {value}\n"
            pckt_ts = []
        mybyte = file.read(1)
        p += 1
        continue
    # next 8 bytes: TIMESTAMP
    if p > (1 + NUM) and p <= ((1 + NUM) + TS): # 5 and 13
        pckt_ts.append(mybyte)
        if p == ((1 + NUM) + TS): # 13
            b = b''.join(pckt_ts)
            value = (int.from_bytes(b, byteorder='little')) / CLOCK
            s += f"TIME({TS}): {pckt_ts} = {value} micro(s)\n"
            pckt_len = []
        mybyte = file.read(1)
        p += 1
    # next 2 bytes: LENGTH
    if p > ((1 + NUM) + TS) and p <= (((1 + NUM) + TS) + LEN): # 13 and 15
        pckt_len.append(mybyte)
        if p == (((1 + NUM) + TS) + LEN): # 15
            b = b''.join(pckt_len)
            # length value includes the status bytes (2) if bit0 = 1 from packt info
            value = int.from_bytes(b, byteorder='little')
            s += f"LEN({LEN}): {pckt_len} = {value}\n"
            pckt_payload = []
        mybyte = file.read(1)
        p += 1
    # next 1 byte: PAYLOAD LENGTH
    if p == (((1 + NUM) + TS) + LEN + 1): # 16
        N = int(mybyte[::-1].hex(), 16)
        mybyte = file.read(1)
        p += 1
    # next n bytes: PAYLOAD
    # (((1 + NUM) + TS) + LEN + 1) = 16
    if p > (((1 + NUM) + TS) + LEN + 1) and p <= ((((1 + NUM) + TS) + LEN + 1) + N): # 16 and (16 + N)
        pckt_payload.append(mybyte)
        if p == ((((1 + NUM) + TS) + LEN + 1) + N): # (16 + N)
            s += f"PAYLOAD({N}): {pckt_payload}\n"

            # rssi included in length: rssi included in payload (BYTE 1)
            rssi = int.from_bytes(pckt_payload[-2], byteorder='little', signed=True)
            s += f"RSSI(BYTE 1): {rssi}\n"

            # crc ok included in length: (BYTE 2, bit7)
            binary_string = "{:08b}".format(int(pckt_payload[-1].hex(), 16))
            inv = binary_string[::-1]
            bit7 = inv[-1] # last bit or bit7
            ok = "1"
            test = int.from_bytes(pckt_payload[-1], byteorder='little', signed=True)
            if bit7 == '0':
                ok = "0"
            s += f"CRC OK (BYTE 2, bit7): {ok}\n"
            pckt_status = []
        mybyte = file.read(1)
        p += 1
    # next 2 bytes: STATUS BYTES
    if p > ((((1 + NUM) + TS) + LEN + 1) + N) and p <= ((((1 + NUM) + TS) + LEN + 1) + N + STATUS): # (16 + N) and (16 + N + 2)
        pckt_status.append(mybyte)
        if p == ((((1 + NUM) + TS) + LEN + 1) + N + STATUS): # 16 + N + 2
            s += f"STATUS({STATUS}): [RSSI: {pckt_status[0]}, CORR/LQI: {pckt_status[1]}]\n"
            pckt_spare = []
        mybyte = file.read(1)
        p += 1
    # remaining bytes: SPARE
    if p > ((((1 + NUM) + TS) + LEN + 1) + N + STATUS) and p <= (SPARE + (((1 + NUM) + TS) + LEN)): # (16 + N + 2) and (136+15)
        pckt_spare.append(mybyte)
        if p == (SPARE + (((1 + NUM) + TS) + LEN)): # (136 + 15)
            s += f"SPARE({ (136 - (N + 2 + 1)) }): {pckt_spare}\n"
            p = 1
            starting = True
            pckt_num = []
            pckt_ts = []
            pckt_len = []
            pckt_payload = []
            pckt_status = []
            pckt_spare = []
            mybyte = file.read(1)
            N = 1
            c += 1
            continue
        mybyte = file.read(1)
        p += 1
    #s += f"hex: {h} = {value}\n"

f = open("out.txt", "a")
f.write(s)
f.close()



