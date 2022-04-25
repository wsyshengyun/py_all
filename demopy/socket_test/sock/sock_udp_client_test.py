# -*- coding: utf-8 -*-
'''
@File    :   sock_udp_client_test.py
@Time    :   2021/09/21 22:42:50
'''

import socket

ip_port = ('127.0.0.1', 9999)
sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

while True:
    inp = input("发送的消息： ").strip()
    sk.sendto(inp.encode(), ip_port)
    if inp == 'exit':
        break
sk.close()
