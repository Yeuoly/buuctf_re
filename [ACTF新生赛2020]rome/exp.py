targets = b'Qsw3sj_lz4_Ujw@l'

def searchAscii(remainder):
    if remainder >= 97 and remainder <= 122:
        for i in range(20):
            res = ((remainder - 97) + i * 26) + 79
            if(res >= 97 and res <= 122):
                return res
    elif remainder >= 65 and remainder <= 90:
        for i in range(20):
            res = ((remainder - 65) + i * 26) + 51
            if(res >= 65 and res <= 90):
                return res
    return remainder

print('flag{' + bytearray([searchAscii(i) for i in targets]).decode() + '}')