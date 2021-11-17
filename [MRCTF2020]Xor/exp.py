origin = b'\x4dSAWB~FXZ:J:`tQJ"N@ bpdd}8g'

flag = bytearray([origin[i] ^ i for i in range(len(origin))])
print(flag.decode())