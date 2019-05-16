import socket
import cvxpy
import numpy as np

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("59.106.212.75", 8081))

s.recv(261)

for i in range(120):
    data = s.recv(200)
    n = int(data.rstrip())
    print (n)
    j = 2
    while (j * j) <= n:
        while n % j == 0:
            n = n // j
        j = j + 1
    print (n)
    s.send(str(n).encode() + "\n".encode())
