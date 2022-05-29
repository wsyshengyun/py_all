# coding:utf8

import socket
import sys


def socket_client():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('127.0.0.1', 6667))

    except socket.error as msg:
        print(msg)
        sys.exit(1)

    print(s.recv(1024).decode())

    while True:
        data = input("请输入一些数据发送给服务端: ")

        data_a = "客户端: 我将发送的数据给服务端: {}".format(data)
        data_bstr = data.encode()
        # 客户端发送数据到服务器
        s.send(data_bstr)

        if data == 'exit':
            break

        # 客户端接收数据
        data_from_service = s.recv(1024)
        print('客户端: 我接收服务端的数据为 ', data_from_service.decode('utf8'))

    # 套接字关闭
    s.close()


# if __name__ == '__main__':
socket_client()
