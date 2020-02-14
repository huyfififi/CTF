import socket
import subprocess
import base64

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("challenges.neverlanctf.com", 1120))

# data = s.recv(1000)
for i in range(200000):
    data = s.recv(1000)
    print(data)
    data = str(data).split(' ')[-1][:-1]
    print(data)
    proc = base64.b64decode(data)
    print(proc)
    s.send(proc)
    data = s.recv(1000)
    print(data)
