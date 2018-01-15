import socket
import sys
host = 'www.baidu.com'
port = 80
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    remote_ip = socket.gethostbyname(host)#获取远程主机的IP：
    # print(host+remote_ip)
except socket.gaierror:
    sys.exit()

print(remote_ip)
