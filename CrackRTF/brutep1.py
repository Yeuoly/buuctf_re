from hashlib import md5, sha1

for i in range(100000, 1000000):
    if sha1('{}@DBApp'.format(i).encode()).hexdigest() == '6e32d0943418c2c33385bc35a1470250dd8923a9':
        password_1 = str(i)
        break

AAA = [0x05, 0x7D, 0x41, 0x15, 0x26, 0x01]
rtf_header = b'{\\rtf1'


password_2 = bytearray([(int(rtf_header[i]) ^ AAA[i]) for i in range(6)])

print('password_1 : ' + password_1)

print('password_2 : ' + password_2.decode())

