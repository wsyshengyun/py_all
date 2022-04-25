# -*- coding: utf-8 -*-
'''
@File    :   socket_client_test.py
@Time    :   2021/09/21 21:42:48
'''

import socket

SIZE_ACCAPT = 1024
ip_port = ('127.0.0.1', 9999)
s = socket.socket()  # 创建套接字
s.connect(ip_port)  # 连接服务器
while True:  # 通过一个死循环不断接收用户输入，并发送给服务器
    inp = input("请输入你要发送的信息： ".strip())
    if not inp:  # 防止输入空信息，导致异常退出
        continue
    s.sendall(inp.encode())

    if inp == 'exit':  # 如果输入的是'exit'，表示断开连接
        print("通信结束！")
        break
    server_reply = s.recv(SIZE_ACCAPT).decode()
    print(server_reply)

s.close()
