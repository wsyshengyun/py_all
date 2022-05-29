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
    print('服务端: 我与{} 建立一个新的连接'.format(addr))
    conn.send('服务端说: 欢迎!'.encode())

    while True:
        # 服务端 接受数据
        data = conn.recv(1024)
        # 数据解码后再打印输出
        print('服务端: 接收自{} 的数据:{}'.format(addr, data.decode()))
        time.sleep(1)
        # 如果原数据为exit则退出此循环
        if data == b'exit' or not data:
            conn.send(bytes('数据>来自服务端的语言: 关闭把', 'UTF-8'))
            break
        # 服务端发送数据到客户端 data的格式为 bytes~
        send_str = '服务端: 我接收了你的数据,数据将原路返回: '.format(data)
        # conn.send(bytes(send_str, 'UTF-8'))
        conn.send(data)
    # 当退出循环的时候连接关闭
    conn.close()


# if __name__ == '__main__':
socket_service()
