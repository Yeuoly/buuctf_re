targets = [180, 136, 137, 147, 191, 137, 147, 191, 148, 136, 133, 191, 134, 140, 129, 135, 191, 65]

flag = ''

for i in targets:
    flag += chr(( i ^ 32 ) - ord('@'))

print(flag)