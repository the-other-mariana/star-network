import numpy as np
from fcf_type_codes import TYPES as fcft
import pandas as pd

filename = 'tests/TestWireless_1_160422.psd'
file = open(filename,'rb')
mybyte = file.read(1)

s = ""
c = 0
p = 1

# CC2531EMK CLOCK
CLOCK = 32

LONG_LENGTH = 8
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

# dataframe info
columns = ['FCS', 'CORR', 'BUFF_OVERFLOW', 'GENERIC',
           'PCKT_NUM', 'TIME(MS)', 'LENGTH', 'PAYLOAD', 'RSSI', 'CRC_OK',
           'FRAME_TYPE', 'DEST_PAN', 'DEST_ADD', 'SRC_PAN', 'SRC_ADD']
df = pd.DataFrame(columns=columns)
row = {col: '' for col in columns}
first = True

# 11 9 9 11 10
# 11(+54) = 65, 9(+51) = 60, 10+(53) = 63 (LQI)
# 11(-73) = -62, 9(-73) = -64, 10(-73) = -63 (RSSI)

while mybyte:
    if c == 150: break
    # first byte: PACKET INFO
    if p == 1:

        s += "================\n"
        s += "PCKT INFO\n"
        binary_string = "{:08b}".format(int(mybyte.hex(), 16))
        inv = binary_string[::-1]
        used_bits = inv[:4]
        if used_bits[0] == '1':
            s += 'FCS: true '
            row['FCS'] = 1
        else:
            s += 'FCS: false '
            row['FCS'] = 0
        if used_bits[1] == '1':
            s += 'CORR: 1 '
            row['CORR'] = 1
        else:
            s += 'CORR: 0 '
            row['CORR'] = 0
        if used_bits[2] == '1':
            s += 'BUFF_OVERFLOW: true '
            row['BUFF_OVERFLOW'] = 1
        else:
            s += 'BUFF_OVERFLOW: false '
            row['BUFF_OVERFLOW'] = 0
        if used_bits[3] == '1':
            s += 'GENERIC: true '
            row['GENERIC'] = 1
        else:
            s += 'GENERIC: false '
            row['GENERIC'] = 0
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
            row['PCKT_NUM'] = value
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
            row['TIME(MS)'] = value
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
            row['LENGTH'] = value
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

            byte0 = "{:08b}".format(int(pckt_payload[0].hex(), 16))[::-1]
            byte1 = "{:08b}".format(int(pckt_payload[1].hex(), 16))[::-1]
            # frame control field
            # Bit0-2: TYPE (invert)
            fcf_type = byte0[:3][::-1]
            pan_compr = byte0[6]
            dest_add_mode = ''.join([byte1[3], byte1[2]])
            src_add_mode = ''.join([byte1[7], byte1[6]])
            s += f"Add Mode: {byte0} {byte1}\n"
            b = 3

            if fcf_type == fcft['CMD'] or fcf_type == fcft['DATA'] or fcf_type == fcft['BCN'] or fcf_type == fcft['1_OCT_HEADER'] or fcf_type == fcft['RFID_BLINK']:
                key = list(fcft.keys())[list(fcft.values()).index(fcf_type)]
                row['FRAME_TYPE'] = key
                if dest_add_mode != '00':
                    dest_pan = b''.join([pckt_payload[b + 1], pckt_payload[b]])
                    row['DEST_PAN'] = '0x' + dest_pan.hex()
                    s += f"\tDest PAN: {'0x' + dest_pan.hex()}\n"
                    b += 2
                if dest_add_mode != '00' and src_add_mode != '00':
                    if dest_add_mode == '11':
                        # long address
                        dest_add = b''.join(pckt_payload[b:(b + LONG_LENGTH)][::-1])
                        row['DEST_ADD'] = '0x' + dest_add.hex()
                        s += f"\tDest Add: {'0x' + dest_add.hex()}\n"
                        b += 8
                    else:
                        # short address
                        dest_add = b''.join([pckt_payload[b + 1], pckt_payload[b]])
                        row['DEST_ADD'] = '0x' + dest_add.hex()
                        s += f"\tDest Add: {'0x' + dest_add.hex()}\n"
                        b += 2
                if src_add_mode != '00' and pan_compr == '0':
                    src_pan = b''.join([pckt_payload[b + 1], pckt_payload[b]])
                    row['SRC_PAN'] = '0x' + src_pan.hex()
                    s += f"\tSrc PAN: {'0x' + src_pan.hex()}\n"
                    b += 2
                if src_add_mode != '00':
                    if src_add_mode == '11':
                        # long address
                        src_add = b''.join(pckt_payload[b:(b + LONG_LENGTH)][::-1])
                        row['SRC_ADD'] = '0x' + src_add.hex()
                        s += f"\tSrc Add: {'0x' + src_add.hex()}\n"
                        b += 8
                    else:
                        # short address
                        src_add = b''.join([pckt_payload[b + 1], pckt_payload[b]])
                        row['SRC_ADD'] = '0x' + src_add.hex()
                        s += f"\tSrc Add: {'0x' + src_add.hex()}\n"
                        b += 2
            # type ACK: 1 length: 5
            if fcf_type == fcft['ACK']:
                if len(pckt_payload) == 5:
                    # no fields with addresses
                    row['FRAME_TYPE'] = 'ACK'
                    pass
                else:
                    row['FRAME_TYPE'] = 'ACK'
                    s += f"ACK packet with unexpected length\n"
            # type R111, R100
            if fcf_type == fcft['CSL_WAKEUP']:
                row['FRAME_TYPE'] = 'CSL_WAKEUP'
                dest_pan = b''.join([pckt_payload[5], pckt_payload[4]])
                dest_add = b''.join([pckt_payload[7], pckt_payload[6]])

                row['DEST_PAN'] = '0x' + dest_pan.hex()
                row['DEST_ADD'] = '0x' + dest_add.hex()
                s += f"\tDest PAN: {'0x' + dest_pan.hex()}\n\tDest Add: {'0x' + dest_add.hex()}\n"
            if fcf_type == fcft['CSL_SECURE_ACK']:
                row['FRAME_TYPE'] = 'CSL_SECURE_ACK'
                dest_pan = b''.join([pckt_payload[5], pckt_payload[4]])
                dest_add = b''.join([pckt_payload[7], pckt_payload[6]])

                row['DEST_PAN'] = '0x' + dest_pan.hex()
                row['DEST_ADD'] = '0x' + dest_add.hex()
                s += f"\tDest PAN: {'0x' + dest_pan.hex()}\n\tDest Add: {'0x' + dest_add.hex()}\n"


            '''
            # type CMD: 5 lengths: 10, 21, 18, 27, 12
            if fcf_type == fcft['CMD']:
                if len(pckt_payload) == 10:
                    dest_pan = b''.join([pckt_payload[4], pckt_payload[3]])
                    dest_add = b''.join([pckt_payload[6], pckt_payload[5]])
                    s += f"\tDest PAN: {'0x' + dest_pan.hex()}\n\tDest Add: {'0x' + dest_add.hex()}\n"
                    row['FRAME_TYPE'] = 'CMD'
                    row['DEST_PAN'] = '0x' + dest_pan.hex()
                    row['DEST_ADD'] = '0x' + dest_add.hex()
                    row['SRC_PAN'] = ''
                    row['SRC_ADD'] = ''
                elif len(pckt_payload) == 21:
                    dest_pan = b''.join([pckt_payload[4], pckt_payload[3]])
                    dest_add = b''.join([pckt_payload[6], pckt_payload[5]])
                    src_pan = b''.join([pckt_payload[8], pckt_payload[7]])
                    src_add = b''.join(pckt_payload[9:(9 + LONG_LENGTH)][::-1])
                    s += f"\tDest PAN: {'0x' + dest_pan.hex()}\n\tDest Add: {'0x' + dest_add.hex()}\n\tSrc PAN: {'0x' + src_pan.hex()}\n\tSrc Add: {'0x' + src_add.hex()}\n"
                    row['FRAME_TYPE'] = 'CMD'
                    row['DEST_PAN'] = '0x' + dest_pan.hex()
                    row['DEST_ADD'] = '0x' + dest_add.hex()
                    row['SRC_PAN'] = '0x' + src_pan.hex()
                    row['SRC_ADD'] = '0x' + src_add.hex()
                elif len(pckt_payload) == 18:
                    dest_pan = b''.join([pckt_payload[4], pckt_payload[3]])
                    dest_add = b''.join([pckt_payload[6], pckt_payload[5]])
                    src_add = b''.join(pckt_payload[7:(7 + LONG_LENGTH)][::-1])
                    s += f"\tDest PAN: {'0x' + dest_pan.hex()}\n\tDest Add: {'0x' + dest_add.hex()}\n\tSrc Add: {'0x' + src_add.hex()}\n"
                    row['FRAME_TYPE'] = 'CMD'
                    row['DEST_PAN'] = '0x' + dest_pan.hex()
                    row['DEST_ADD'] = '0x' + dest_add.hex()
                    row['SRC_PAN'] = ''
                    row['SRC_ADD'] = '0x' + src_add.hex()
                elif len(pckt_payload) == 27:
                    dest_pan = b''.join([pckt_payload[4], pckt_payload[3]])
                    dest_add = b''.join(pckt_payload[5:(5 + LONG_LENGTH)][::-1])
                    src_add = b''.join(pckt_payload[((5 + LONG_LENGTH) + 1):((5 + LONG_LENGTH) + 1 + LONG_LENGTH)][::-1])
                    s += f"\tDest PAN: {'0x' + dest_pan.hex()}\n\tDest Add: {'0x' + dest_add.hex()}\n\tSrc Add: {'0x' + src_add.hex()}\n"
                    row['FRAME_TYPE'] = 'CMD'
                    row['DEST_PAN'] = '0x' + dest_pan.hex()
                    row['DEST_ADD'] = '0x' + dest_add.hex()
                    row['SRC_PAN'] = ''
                    row['SRC_ADD'] = '0x' + src_add.hex()
                elif len(pckt_payload) == 12:
                    dest_pan = b''.join([pckt_payload[4], pckt_payload[3]])
                    dest_add = b''.join([pckt_payload[6], pckt_payload[5]])
                    src_add = b''.join([pckt_payload[8], pckt_payload[7]])
                    s += f"\tDest PAN: {'0x' + dest_pan.hex()}\n\tDest Add: {'0x' + dest_add.hex()}\n\tSrc Add: {'0x' + src_add.hex()}\n"
                    row['FRAME_TYPE'] = 'CMD'
                    row['DEST_PAN'] = '0x' + dest_pan.hex()
                    row['DEST_ADD'] = '0x' + dest_add.hex()
                    row['SRC_PAN'] = ''
                    row['SRC_ADD'] = '0x' + src_add.hex()
                elif len(pckt_payload) == 107:
                    dest_pan = b''.join([pckt_payload[4], pckt_payload[3]])
                    dest_add = b''.join([pckt_payload[6], pckt_payload[5]])
                    src_add = b''.join([pckt_payload[8], pckt_payload[7]])
                    s += f"\tDest PAN: {'0x' + dest_pan.hex()}\n\tDest Add: {'0x' + dest_add.hex()}\n\tSrc Add: {'0x' + src_add.hex()}\n"
                    row['FRAME_TYPE'] = 'CMD'
                    row['DEST_PAN'] = '0x' + dest_pan.hex()
                    row['DEST_ADD'] = '0x' + dest_add.hex()
                    row['SRC_PAN'] = ''
                    row['SRC_ADD'] = '0x' + src_add.hex()
                else:
                    row['FRAME_TYPE'] = 'CMD'
                    s += f"CMD packet with unexpected length\n"
            # type BCN: 5 lengths: 13, 21, 23, 15, 17 (same fields)
            if fcf_type == fcft['BCN']:
                if len(pckt_payload) == 13 or len(pckt_payload) == 21 or len(pckt_payload) == 23 or len(pckt_payload) == 15 or len(pckt_payload) == 17:
                    src_pan = b''.join([pckt_payload[4], pckt_payload[3]])
                    src_add = b''.join([pckt_payload[6], pckt_payload[5]])
                    s += f"\tSrc PAN: {'0x' + src_pan.hex()}\n\tSrc Add: {'0x' + src_add.hex()}\n"
                    row['FRAME_TYPE'] = 'BCN'
                    row['DEST_PAN'] = ''
                    row['DEST_ADD'] = ''
                    row['SRC_PAN'] = '0x' + src_pan.hex()
                    row['SRC_ADD'] = '0x' + src_add.hex()
                else:
                    row['FRAME_TYPE'] = 'BCN'
                    s += f"BCN packet with unexpected length\n"
            # type ACK: 1 length: 5
            if fcf_type == fcft['ACK']:
                if len(pckt_payload) == 5:
                    # no fields with addresses
                    row['FRAME_TYPE'] = 'ACK'
                    pass
                else:
                    row['FRAME_TYPE'] = 'ACK'
                    s += f"ACK packet with unexpected length\n"
            # type DATA: always different length
            if fcf_type == fcft['DATA']:
                dest_pan = b''.join([pckt_payload[4], pckt_payload[3]])
                dest_add = b''.join([pckt_payload[6], pckt_payload[5]])
                src_add = b''.join([pckt_payload[8], pckt_payload[7]])
                s += f"\tDest PAN: {'0x' + dest_pan.hex()}\n\tDest Add: {'0x' + dest_add.hex()}\n\tSrc Add: {'0x' + src_add.hex()}\n"
                row['FRAME_TYPE'] = 'DATA'
                row['DEST_PAN'] = '0x' + dest_pan.hex()
                row['DEST_ADD'] = '0x' + dest_add.hex()
                row['SRC_PAN'] = ''
                row['SRC_ADD'] = '0x' + src_add.hex()

            # type R111, R100
            if fcf_type not in [fcft['DATA'], fcft['CMD'], fcft['BCN'], fcft['ACK']]: # 108
                dest_pan = b''.join([pckt_payload[4], pckt_payload[3]])
                dest_add = b''.join([pckt_payload[6], pckt_payload[5]])
                src_add = b''.join([pckt_payload[8], pckt_payload[7]])
                s += f"\tDest PAN: {'0x' + dest_pan.hex()}\n\tDest Add: {'0x' + dest_add.hex()}\n\tSrc Add: {'0x' + src_add.hex()}\n"
                row['FRAME_TYPE'] = fcf_type
                row['DEST_PAN'] = '0x' + dest_pan.hex()
                row['DEST_ADD'] = '0x' + dest_add.hex()
                row['SRC_PAN'] = ''
                row['SRC_ADD'] = '0x' + src_add.hex()
            '''

            # failed tests for rssi (?)
            ba = bytearray(pckt_payload[-2])
            arr = np.ndarray(shape=(1,), dtype='<i1', buffer=ba) # < = little endian, i1 = signed 1 byte integer
            bs = "{:08b}".format(int(pckt_payload[-2].hex(), 16))
            # print(bs)

            # rssi included in length: rssi included in payload (BYTE 1) MUST SUBSTRACT 73
            rssi = int.from_bytes(pckt_payload[-2], byteorder='little', signed=True)
            s += f"RSSI(BYTE 1): {(rssi - 73)}\n"
            row['RSSI'] = (rssi - 73)

            # crc ok included in length: (BYTE 2, bit7)
            binary_string = "{:08b}".format(int(pckt_payload[-1].hex(), 16))
            inv = binary_string[::-1]
            bit7 = inv[-1] # last bit or bit7
            ok = "1"
            test = int.from_bytes(pckt_payload[-1], byteorder='little', signed=True)
            if bit7 == '0':
                ok = "0"
            s += f"CRC OK (BYTE 2, bit7): {ok}\n"
            row['CRC_OK'] = int(ok)
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
    if p == (SPARE + (((1 + NUM) + TS) + LEN)):
        row_df = pd.DataFrame([row])
        df = pd.concat([df, row_df], ignore_index=True, axis=0)
        row = {col: '' for col in columns}

f = open("out.txt", "a")
f.write(s)
f.close()
df.to_csv('csvs/' + (filename.split('/')[1]).split('.')[0] + '.csv')



