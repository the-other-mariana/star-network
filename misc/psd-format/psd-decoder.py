
filename = 'RegistroPrueba_120422.psd'

with open(filename,'rb') as f:
    buff = f.read()
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




