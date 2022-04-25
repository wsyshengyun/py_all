# -*- coding: utf-8 -*-
'''
@File    :   queuetest.py
@Time    :   2020/09/26 07:13:05
'''

""" 
pw.terminate() 
 """

import time
from multiprocessing import Process, Queue


def write(q):
    for i in ['a', 'b', 'c', 'd', 'e']:
        print('Put %s to queue' % i)
        q.put(i)
        time.sleep(0.5)


def read(q):
    while True:
        time.sleep(1)
        v = q.get(True)
        print("get %s from queue" % v)


def main():
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    print("write process = ", pw)
    print("read process = ", pr)
    pw.start()
    pr.start()
    pw.join()
    pr.join()
    pr.terminate()
    pw.terminate()
    print("end....")


if __name__ == '__main__':
    main()
