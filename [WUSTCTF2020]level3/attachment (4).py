from base64 import b64decode

std = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=')
charset = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=')

for i in range(9):
    tmp = charset[i]
    charset[i] = charset[19 - i]
    charset[19 - i] = tmp

origin = list('d2G0ZjLwHjS7DmOzZAY0X2lzX3CoZV9zdNOydO9vZl9yZXZlcnGlfD==')

for i in range(len(origin)):
    origin[i] = std[charset.index(origin[i])]

print(b64decode(str(origin)).decode())