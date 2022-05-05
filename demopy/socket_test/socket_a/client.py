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

    print(s.recv(1024))

    while True:
        data = input("please input work: ").encode()
        s.send(data)
        print('aa', s.recv(1024))
        if data == b'exit':
            break

    s.close()


# if __name__ == '__main__':
socket_client()
