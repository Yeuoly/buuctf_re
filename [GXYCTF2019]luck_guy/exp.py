flag_1 = 'GXY{do_not_'
flag_2_origin = [0x69, 0x63, 0x75, 0x67, 0x60, 0x6f, 0x66, 0x7f]

for i in range(8):
    if i & 1:
        flag_2_origin[i] -= 2
    else:
        flag_2_origin[i] -= 1

flag_2 = bytearray(flag_2_origin).decode()

print(flag_1 + flag_2)