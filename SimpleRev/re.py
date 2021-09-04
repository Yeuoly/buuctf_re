dest = 'killshadow'
charset = 'adsfkndcls'

def search(i):
    t = ord(dest[i]) - 97
    d = 0
    while True:
        c = t + 26 * d
        ipt = c + 39 + ord(charset[i]) - 97
        if ipt in range(ord('A'), ord('Z') + 1):
            return chr(ipt)
        d = d + 1

flag = ''
for i in range(len(dest)):
    flag += search(i)

print('flag{' + flag + '}')