flag = 'pvkq{m164675262033l4m49lnp7p9mnk28k75}'

def parse(c):
    if (c < 'A' or c > 'Z') and (c < 'a' or c > 'z'):
        return ord(c)
    else:
        c = chr(ord(c) + 16)
        if ((c > 'Z' and c < 'a') or c >= 'z'):
            return ord(c) - 26


flag = bytearray([parse(i) for i in flag]).decode()

print(flag)