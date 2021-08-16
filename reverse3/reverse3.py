from base64 import b64decode

source = 'e3nifIH9b_C@n@dH'
middle = ''

for i in range(16):
    middle += chr(ord(source[i]) - i)
    
print(b64decode(middle).decode())
