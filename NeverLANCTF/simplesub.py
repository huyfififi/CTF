string = "MKXU IDKMI DM BDASKMI NLU XCPJNDICFQ! K VDMGUC KW PDT GKG NLKB HP LFMG DC TBUG PDTC CUBDTCXUB. K'Q BTCU MDV PDT VFMN F WAFI BD LUCU KN KB WAFI GDKMINLKBHPLFMGKBQDCUWTMNLFMFMDMAKMUNDDA"

print (string)

s = list(string)

for i in range(len(s)):
    if s[i] == "A":
        s[i] = "l"
    elif s[i] == "B":
        s[i] = "s"
    elif s[i] == "C":
        s[i] = "r"
    elif s[i] == "D":
        s[i] = "o"
    elif s[i] == "E":
        s[i] = "E"
    elif s[i] == "F":
        s[i] = "a"
    elif s[i] == "G":
        s[i] = "d"
    elif s[i] == "H":
        s[i] = "b"
    elif s[i] == "I":
        s[i] = "g"
    elif s[i] == "J":
        s[i] = "p"
    elif s[i] == "K":
        s[i] = "i"
    elif s[i] == "L":
        s[i] = "h"
    elif s[i] == "M":
        s[i] = "n"
    elif s[i] == "N":
        s[i] = "t"
    elif s[i] == "O":
        s[i] = "O"
    elif s[i] == "P":
        s[i] = "y"
    elif s[i] == "Q":
        s[i] = "m"
    elif s[i] == "R":
        s[i] = "R"
    elif s[i] == "S":
        s[i] = "v"
    elif s[i] == "T":
        s[i] = "u"
    elif s[i] == "U":
        s[i] = "e"
    elif s[i] == "V":
        s[i] = "w"
    elif s[i] == "W":
        s[i] = "f"
    elif s[i] == "X":
        s[i] = "c"
    elif s[i] == "Y":
        s[i] = "Y"
    elif s[i] == "Z":
        s[i] = "Z"

string = "".join(s)
print (string)
