# -*- coding: utf-8 -*-
'''
@File    :   sock_udp_server_test.py
@Time    :   2021/09/21 22:45:17
'''

import socket

ip_port = ('127.0.0.1', 9999)
sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0) 
sk.bind(ip_port)

while True:
    data = sk.recv(1024).strip().decode()
    print(data)
    if data=='exit':
        print("客户端主动断开连接！")
        break
    sk.close() 