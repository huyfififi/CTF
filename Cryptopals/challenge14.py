#Detect single-character XOR

import binascii

f = open("4.txt")

#key-size = 1byte(8bit) one character ascii 8bit
KEY_SIZE = 8

'''===my scoring==='''
def plain_text_score (string):
    score = 0
    for i in range (len(string)):
        #if A~Z score++
        if string[i] >= 65 and string[i] <= 90:
            score = score + 1
        #if a~z score++
        elif string[i] >= 97 and string[i] <= 122:
            score = score + 1
        #if SPC or " or ' score++
        elif string[i] == 32 or string[i] == 34 or string[i] == 39:
            score = score + 1
    return score

if __name__ == "__main__":
    max_score = 0
    message = ""

    #for all lines in file
    for s_line in f:
        encrypted_hexstring = s_line

        #key might be 0~2^8
        for i in range (2**KEY_SIZE):

            decrypted = ""

            key_bin = bin(i)[2:]
        
            while len(key_bin) < KEY_SIZE:
                key_bin = "0" + key_bin

            for i in range (len(encrypted_hexstring) // 2):
                #2*i~2*i+1 xor 1 byte
                enc_bin = bin(int(encrypted_hexstring[(2*i):(2*i+2)], 16))[2:]
                while len(enc_bin) < KEY_SIZE:
                    enc_bin = "0" + enc_bin

                xored = int(key_bin, 2) ^ int(enc_bin, 2)
                xored_bin = bin(xored)[2:]
                while len(xored_bin) < KEY_SIZE:
                    xored_bin = "0" + xored_bin

                #split and decrypt
                decrypted = decrypted + hex(int(xored_bin[0:4], 2))[2:] + hex(int(xored_bin[4:8], 2))[2:]

            possible_message = binascii.unhexlify(decrypted)
            score = plain_text_score(possible_message)
            if score > max_score:
                max_score = plain_text_score(possible_message)
                message = possible_message


    print (message)
    #b'Now that the party is jumping\n'
