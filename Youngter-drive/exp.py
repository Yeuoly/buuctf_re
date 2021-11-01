target = 'TOiZiZtOrYaToUwPnToBsOaOapsyS'

charset = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'

flag = ''

for i in range(29):
    if i & 1 == 0:
        flag += target[i]
        continue
    idx = charset.index(target[i])
    if chr(idx + 96).islower():
        flag += chr(idx + 96)
    else:
        flag += chr(idx + 38)

print(flag + 'E')