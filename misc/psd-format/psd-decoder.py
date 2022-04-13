
filename = 'RegistroPrueba_120422.psd'
file = open(filename,'rb')
mybyte = file.read(1)

s = ""
c = 0
p = 1
starting = True
pckt_num = []
pckt_ts = []
pckt_len = []
pckt_payload = []
pckt_status = []
pckt_spare = []
while mybyte:
    if c == 100: break
    # first byte: PACKET INFO
    if p == 1:
        s += "PInfo\n"
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
    if p > 1 and p <= 5:
        pckt_num.append(mybyte)
        if p == 5:
            s += f"NUM: {pckt_num}\n"
            pckt_ts = []
        mybyte = file.read(1)
        p += 1
        continue
    # next 8 bytes: TIMESTAMP
    if p > 5 and p <= 13:
        pckt_ts.append(mybyte)
        if p == 13:
            s += f"TIME: {pckt_ts}\n"
            pckt_len = []
        mybyte = file.read(1)
        p += 1
    # next 2 bytes: LENGTH
    if p > 13 and p <= 15:
        pckt_len.append(mybyte)
        if p == 15:
            s += f"LEN: {pckt_len}\n"
            pckt_payload = []
        mybyte = file.read(1)
        p += 1
    # next 1 byte: PAYLOAD LENGTH
    if p == 16:
        N = int(mybyte[::-1].hex(), 16)
        mybyte = file.read(1)
        p += 1
    # next n bytes: PAYLOAD
    if p > 16 and p <= (16 + N):
        pckt_payload.append(mybyte)
        if p == (16 + N):
            s += f"PAYLOAD: {pckt_payload}\n"
            pckt_status = []
        mybyte = file.read(1)
        p += 1
    # next 2 bytes: STATUS BYTES
    if p > (16 + N) and p <= (16 + N + 2):
        pckt_status.append(mybyte)
        if p == (16 + N + 2):
            s += f"STATUS: [RSSI: {pckt_status[0]}, CORR/LQI: {pckt_status[1]}]\n"
            pckt_spare = []
        mybyte = file.read(1)
        p += 1
    if p >


    #s += f"hex: {h} = {value}\n"

    mybyte = file.read(1)
    c+=1

f = open("decimal.txt", "a")
f.write(s)
f.close()
'''
with open(filename,'rb') as f:
    buff = f.read()
    print(buff)
# the hex representation of each byte
out_hex = ['{:02X}'.format(b) for b in buff]

s = ""
for h in out_hex[:10]:
    mybyte = bytes.fromhex(h)
    binary_string = "{:08b}".format(int(mybyte.hex(), 16))
    print(f"hex: {h} = {int('0000' + binary_string[:4], 16)}," + f"{int('0000'+binary_string[4:], 16)} ")
    print(f"src: {binary_string[:4]}, {binary_string[4:]}")
    s += f"hex: {h} = {int('0000' + binary_string[:4], 16)}," + f"{int('0000'+binary_string[4:], 16)} "

f = open("decimal.txt", "a")
f.write(s)
f.close()
'''



