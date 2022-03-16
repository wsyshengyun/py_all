# -*- coding: utf-8 -*-
'''
@File    :   sock_alladdress.py
@Time    :   2021/09/21 23:07:36
'''

import socket

class MySocket(object):
    size = 1024
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port 
        self.sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)


class MySocketClient(MySocket):
    def __init__(self, ip, port):
        super().__init__(ip, port)
        con = self.sk.connect((self.ip, self.port))
        print("客户端con is :{}".format(con))


    def start(self):
        while True:
            inp = input("请输入你要发送的信息： ").strip()
            if not inp:
                continue
            elif inp == 'exit':
                print("客户端通信结束！") 
                break
            else:
                self.sk.sendall(inp.encode())
                server_reply = self.sk.recv(self.size).decode() 
                print(server_reply)
        self.sk.close()




class MySocketServer(MySocket):
    def __init__(self, ip, port):
        super().__init__(ip, port)
        self.sk.bind((self.ip, self.port))

    def start(self):
        self.sk.listen(10) # 最大监听数，允许多少人在排队
        print("开始监听")
        conn, addr = self.sk.accept()
        while True:
            client_data = conn.recv(self.size).decode()
            if client_data == 'exit':
                break

            print("接收来自{}：{} 客户端发来的信息：{}".format(addr[0], addr[1], client_data))
            conn.sendall("服务器已经收到你的信息.".encode())
        self.sk.close()
        exit("通信结束~")



    