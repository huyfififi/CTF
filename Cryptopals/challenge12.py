#Fixed XOR

import binascii #bonus

def xor (buf1, buf2):
    return buf1 ^ buf2

if __name__ == "__main__":

    str1 = 0x1c0111001f010100061a024b53535009181c
    str2 = 0x686974207468652062756c6c277320657965 

    xored = xor (str1, str2)
    xored_hex = hex(xored)

    print (xored_hex)
    #0x746865206b696420646f6e277420706c6179

    '''bonus'''
    decoded = binascii.unhexlify(xored_hex[2:])
    print (decoded)
    #b"the kid don't play"

