# uncompyle6 version 3.7.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.8.10 (default, Jun  2 2021, 10:49:15) 
# [GCC 9.4.0]
# Embedded file name: encode.py
# Compiled at: 2019-08-19 21:01:57
print('Welcome to Re World!')
print('Your input1 is your flag~')

input1 = ''

l = len(input1)
for i in range(l):
    num = ((ord(input1[i]) + i) % 128 + 128) % 128 # ord(input1[i] + i) % 128
    code += num

for i in range(l - 1):
    code[i] = code[i] ^ code[(i + 1)]

print code
code = ['\x1f', '\x12', '\x1d', '(', '0', '4', '\x01', '\x06', '\x14', '4', ',', '\x1b', 'U', '?', 'o', '6', '*', ':', '\x01', 'D', ';', '%', '\x13']
# okay decompiling attachment.pyc
