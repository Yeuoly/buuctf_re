from base64 import b64decode

enc = 'zMXHz3TIgnxLxJhFAdtZn2fFk3lYCrtPC2l9'.swapcase()
model = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
changed_model = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/')
for i in range(6, 15):
    changed_model[i], changed_model[i + 10] = changed_model[i + 10], changed_model[i]

changed_model = ''.join(changed_model)

dec = ''
for i in enc:
    dec += model[changed_model.index(i)]

print(b64decode(dec).decode())