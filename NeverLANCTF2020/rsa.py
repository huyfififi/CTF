def exgcd(m, n):
  if n>0:
    y,x,d = exgcd(n, m%n)
    return x, y-m//n*x, d
  else:
    return 1, 0, m


c = '2193 1745 2164 970 1466 2495 1438 1412 1745 1745 2302 1163 2181 1613 1438 884 2495 2302 2164 2181 884 2302 1703 1924 2302 1801 1412 2495 53 1337 2217'.split()
e = 569
n = 2533
p1 = 17
p2 = 149
d = exgcd(e, (p1-1)*(p2-1))[0] % ((p1-1)*(p2-1))

for char in c:
    char = int(char)
    p = pow(char, d, n)
    p = hex(p)[2:]
    str1 = bytes.fromhex(p).decode()
    print(str1, end='')
