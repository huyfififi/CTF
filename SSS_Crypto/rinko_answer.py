n = 493
d = 299

if __name__ == "__main__":
    f = open("cipher.txt")
    c = f.read()
    c = c.split(" ")

    m = ""

    for i in range(len(c) - 1):
        c[i] = bin(pow(int(c[i]), d, n))[2:]
        while len(c[i]) < 5:
            c[i] = "0" + c[i]
        m = m + c[i]

    for i in range(len(m) // 8):
        print (chr(int(m[8*i:8*i+8], 2)), end="")
    print ();
