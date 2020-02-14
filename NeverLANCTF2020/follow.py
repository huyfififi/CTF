import subprocess

url = 'https://7aimehagbl.neverlanctf.com'

for i in range(100000000):
    proc = subprocess.run(["curl", url],stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    print(proc.stdout.decode("utf8"))
    utl = proc.stdout.decode('utf8').split(' ')[3]
