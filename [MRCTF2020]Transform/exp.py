targets = [0x67, 0x79, 0x7B, 0x7F, 0x75, 0x2B, 0x3C, 0x52, 0x53, 0x79, 0x57
    , 0x5E, 0x5D, 0x42, 0x7B, 0x2D, 0x2A, 0x66, 0x42, 0x7E, 0x4C, 0x57
    , 0x79, 0x41, 0x6B, 0x7E, 0x65, 0x3C, 0x5C, 0x45, 0x6F, 0x62, 0x4D, 0x3F, 0x00]

mapsets = [9, 0x0A, 0x0F, 0x17, 0x7, 0x18, 0x0C, 0x6, 0x1, 0x10, 0x3, 0x11, 0x20
    , 0x1D, 0x0B, 0x1E, 0x1B, 0x16, 0x4, 0x0D, 0x13, 0x14, 0x15, 0x2, 0x19
    , 5, 0x1F, 0x8, 0x12, 0x1A, 0x1C, 0x0E, 0x00]

flag = [0] * 64

for i in range(0, 33):
    origin = targets[i] ^ (mapsets[i] & 0xff)
    flag[mapsets[i]] = origin

print(bytearray(flag).decode())