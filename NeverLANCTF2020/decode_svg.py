import binascii

with open('svg.php') as f:
    s = f.read()
    l = s.split("'")
    print(l)
    l = [string[-7:] for string in l if string.startswith("fill")]
    print(l)
    print(len(l))
    l = [string[-1] for string in l]
    print(l)
    bits = ''.join(l) + '0' # padding?
    print(bits)
    print(len(bits), 24**2)
    bits = bits.replace('6', '1')
    print(bits)
    bits = '0b' + bits
    byte = hex(int(bits, 2)).encode()[2:]
    print(byte)
    string = binascii.unhexlify(byte)
    print(string)
