#Implement repeating-key XOR

def string_xor_with_key (keyword, string):
    key_size = len(keyword)
    encoded = ""
    for i in range (len(string)):
        string_bin = bin(ord(string[i]))[2:].zfill(8)
        key_bin = bin(ord(keyword[i % key_size]))[2:].zfill(8)
        xored_bin = bin(int(string_bin, 2) ^ int(key_bin, 2))[2:].zfill(8)
        encoded = encoded + hex(int(xored_bin[0:4], 2))[2:] + hex(int(xored_bin[4:8], 2))[2:]

    return encoded

if __name__ == "__main__":
    string = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    keyword = "ICE"
    
    print (string_xor_with_key (keyword, string))
    #0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f
