import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("zerois-o-reiwa.seccon.jp", 23615))

data = ""
for i in range(200000):
    if i % 2 == 0:
        dust = s.recv(1000)
        print (dust)
    elif i % 2 == 1:
        data = s.recv(1000)
        print (data)
        data = str(data)
        data = data[4:len(data)-5]
        print (data)
        ans = 0
        for i in range(500000):
            tmp = data.replace("?", str(i))
            if eval(tmp) == 0:
                ans = (i)
                break

        print (ans)
        s.send(str(ans).encode() + "\n".encode())
