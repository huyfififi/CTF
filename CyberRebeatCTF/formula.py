import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("59.106.212.75", 8080))

s.recv(261)

for i in range(200):
    data = s.recv(200)
    formula = data.rstrip()
    print (formula)
    ans = (eval(formula))
    print (ans)
    s.send(str(ans).encode() + "\n".encode())
