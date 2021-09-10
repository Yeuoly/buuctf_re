code = ['\x1f', '\x12', '\x1d', '(', '0', '4', '\x01', '\x06', '\x14', '4', ',', '\x1b', 'U', '?', 'o', '6', '*', ':', '\x01', 'D', ';', '%', '\x13']

code = [ord(i) for i in code]

size = len(code)

for i in range(size - 2, -1, -1):
    code[i] = code[i] ^ code[i + 1]

flag = bytearray([(code[i] - i) % 128 for i in range(len(code))]).decode()

print(flag)