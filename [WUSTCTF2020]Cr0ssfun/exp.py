flag = [0] * 0x21

flag[10] = 112
flag[13] = 64
flag[3] = 102 
flag[26] = 114 
flag[20] = 101
flag[7] = 48
flag[16] = 95
flag[11] = 112
flag[23] = 101
flag[30] = 117
flag[0] = 119
flag[6] = 50
flag[22] = 115
flag[31] = 110
flag[12] = 95
flag[15] = 100
flag[8] = 123
flag[18] = 51
flag[28] = 95
flag[21] = 114
flag[2] = 116
flag[9] = 99
flag[32] = 125
flag[19] = 118
flag[5] = 48
flag[14] = 110
flag[4] = 50
flag[17] = 114
flag[29] = 102
flag[17] = 114
flag[24] = 95
flag[1] = 99
flag[25] = 64
flag[27] = 101

print(bytearray(flag).decode())