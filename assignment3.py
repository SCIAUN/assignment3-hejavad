import socket

ports=[21,22,25,80,110,9090]
socket.setdefaulttimeout(5)
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
            if "FreeFloat Ftp Server (Version 1.00)" in ans:
                print("[+] FreeFloat server is vulnerable ", '\n');
            elif "3Com 3CDaemon FTP Server Version 2.0" in ans:
                print("[+] 3CDaemon server is vulnerable ", '\n');
            elif "Ability Server 2.34" in ans:
                print("[+] Ability server is vulnerable ", '\n');
            elif "Sami FTP Server 2.0.2" in ans:
                print("[+] Sami server is vulnerable ", '\n');
            else:
                print("[-] FTP server is not vulnerable", '\n');
        except Exception as e:
            print(e)
