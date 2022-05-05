# coding:utf8
import socket
import threading
import time
import sys


def socket_service():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('127.0.0.1', 6667))
        s.listen(10)
    except socket.error as msg:
        print(msg)
        sys.exit(1)
        pass

    while True:
        conn, addr = s.accept()
        t = threading.Thread(target=deal_data, args=(conn, addr))
        t.start()


def deal_data(conn, addr):
    print('Accept new connection from {}'.format(addr))
    conn.send('Hi, Welcome to the seriver!'.encode())

    while True:
        data = conn.recv(2)
        print('{} client send data is {}'.format(addr, data.decode()))
        time.sleep(1)
        if data == b'exit' or not data:
            conn.send(bytes('Connection closed!', 'UTF-8'))
            break
        conn.send(bytes('Hello, {}'.format(data), 'UTF-8'))
    conn.close()


# if __name__ == '__main__':
socket_service()
