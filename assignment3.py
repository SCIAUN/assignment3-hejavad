import socket

ports=[21,22,25,80,110,9090]
socket.setdefaulttimeout(10)
f=open('host_names','r')
host_names=f.read()
host_names=host_names.split('\n')

for x in host_names:
    print(x)
    for y in ports:
        print(y)
        try:
            s = socket.socket()
            s.connect((x, y))
            ans = s.recv(1024)
            s.close()
            print(ans)
        except Exception as e:
            print(e)
