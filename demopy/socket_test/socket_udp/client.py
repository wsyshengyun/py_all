# coding:utf8
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    msg = "发送消息到服务器".encode('utf8')
    sent = s.sendto(msg, ('localhost', 10000))
    data, server = s.recvfrom(4096)
    print(data.decode())
finally:
    s.close()