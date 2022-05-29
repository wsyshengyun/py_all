# coding:utf8

import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('localhost', 10000))
while 1:
    # 这里与TCP连接不一样么,data不应该是客户端么?clietn
    data, address = sock.recvfrom(4096)
    print(data.decode('utf8'), address)
    if data:
        sent = sock.sendto('已经接受你发来的消息'.encode('utf8'), address)
