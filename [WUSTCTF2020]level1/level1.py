output = [0, 198,232,816,200,1536,300,6144,984,51200,570,92160,1200,565248,756,1474560,800,6291456,1782,65536000]

def char(i, c):
    if not i & 1 == 0:
        return c >> i
    else:
        return c // i
    
flag = bytearray([char(i, output[i]) for i in range(1, len(output))]).decode()

print(flag)