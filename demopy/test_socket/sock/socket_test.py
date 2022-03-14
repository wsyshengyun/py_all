# -*- coding: utf-8 -*-
'''
@File    :   socket_test.py
@Time    :   2021/09/21 15:20:37
'''


import socket
import threading

SIZE_ACCAPT = 1024

def link_handler(link, client):
    while True:  # 一个死循环， 直到客户端发送exit的信号，才关闭连接
        client_data = link.recv(SIZE_ACCAPT).decode() # 接收信息
        if client_data == 'exit':  # 判断是否退出连接
            exit('通信结束')
        print("来自[%s : %s]的客户端向你发来的信息： %s" % (client[0], client[1], client_data))
        link.sendall("服务器已经收到你的信息".encode())# 回馈信息给客户端
    link.close() # 关闭连接

ip_port = ('127.0.0.1', 9999) 

sk = socket.socket()   # 创建套接字
sk.bind(ip_port)  # 绑定服务地址
sk.listen(5) # 监听连接请求
print("启动socket服务，等待客户端连接。。。")
while True:
    conn, address = sk.accept() # 等待连接，此处自动阻塞
    t = threading.Thread(target = link_handler, args=(conn, address))
    t.start()

