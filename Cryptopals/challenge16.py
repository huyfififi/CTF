def string_to_bin (string):
    string_bin = ""
    for i in range (len(string)):
        string_bin = string_bin + bin(ord(string[i]))[2:].zfill(8)
    return string_bin

#Assume that two strings have same length
def hamming (string1, string2):
    hamming_distance = 0
    string1_bin = string_to_bin(string1)
    string2_bin = string_to_bin(string2)
    for i in range (len(string1_bin)):
        if string1_bin[i] != string2_bin[i]:
            hamming_distance = hamming_distance + 1
    return hamming_distance

if __name__ == "__main__":
    string1 = "this is a test"
    string2 = "wokka wokka!!!"
    print (hamming (string1, string2))

'''WIP'''
