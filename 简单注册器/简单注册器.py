x = 'dd2940c04462b4dd7c450528835cca15'
flag = [ord(i) for i in x]

flag[2] = flag[2] + flag[3] - 50
flag[4] = flag[2] + flag[5] - 48
flag[30] = flag[31] + flag[9] - 48
flag[14] = flag[27] + flag[28] - 97

for i in range(16):
    a = flag[31 - i]
    flag[31 - i] = flag[i]
    flag[i] = a

flag = 'flag{' + bytearray(flag).decode() + '}'
print(flag)