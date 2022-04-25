# -*- coding: utf-8 -*-
'''
@File    :   pipetest.py
@Time    :   2020/09/26 07:04:34
'''

""" 以下不懂啊 """

import multiprocessing


def foo(sk):
    sk.send("hello father")
    print(sk.recv())


def main():
    conn1, conn2 = multiprocessing.Pipe()
    p = multiprocessing.Process(target=foo, args=(conn1,))
    p.start()
    print(conn2.recv())
    conn2.send('hi son')


if __name__ == '__main__':
    main()
