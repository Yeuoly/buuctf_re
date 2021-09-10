from base64 import b64decode

byte = [90, 74, 83, 69, 67, 97, 78, 72, 51, 110, 103]

byte.sort()

flag_1 = chr(byte[0] + 34)
flag_2 = chr(byte[4])
flag_3 = b64decode('V1Ax').decode()
flag_4 = b64decode('ak1w').decode()

print('flag{' + flag_1 + flag_2 + flag_3 + flag_4 + '}')