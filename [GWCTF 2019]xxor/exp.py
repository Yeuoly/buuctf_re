from z3 import *

# v7 = [Int('v7[%d]' % i) for i in range(6)]

# s = Solver()

# s.add(v7[0] == 0xDF48EF7E)
# s.add(v7[1] == 0x20CAACF4)
# s.add(v7[2] - v7[4] == 0x42D731A8)
# s.add(v7[5] == 0x84F30420)
# s.add(v7[3] + v7[4] == 0xFA6CB703)
# s.add(v7[2] - v7[3] == 0x84A236FF)

# s.check()
# print(s.model())
v7 = [0] * 6
v7[4] = 2652626477
v7[3] = 1548802262
v7[5] = 2230518816
v7[2] = 3774025685
v7[1] = 550153460
v7[0] = 3746099070

flag = [0] * 6

for i in range(3):
    v4 = v7[i * 2 + 1]
    v3 = v7[i * 2]
    v5 = 0x458bcd42 * 64
    v5 = 0xffffffff & v5
    for i in range(64):
        v4 -= (v3 + v5 + 20) ^ ((v3 << 6) + 3) ^ ((v3 >> 9) + 4) ^ 0x10
        if v4 < 0:
            v4 = 0xffffffff & v4
        v3 -= (v4 + v5 + 11) ^ ((v4 << 6) + 2) ^ ((v4 >> 9) + 2) ^ 0x20
        if v3 < 0:
            v3 = 0xffffffff & v3
        v5 -= 0x458bcd42
        if v5 < 0:
            v5 = 0xffffffff & v5
    
    mask = 0xff000000
    for i in range(4):
        print('%c' % ((v3 & mask) >> (3 - i) * 8), end='')
        mask = mask >> 8
    mask = 0xff000000
    for i in range(4):
        print('%c' % ((v4 & mask) >> (3 - i) * 8), end='')
        mask = mask >> 8