# -*- coding: utf-8 -*-
'''
@File    :   testDaemon.py
@Time    :   2020/09/25 17:53:16
'''


from multiprocessing import Process
from threading import Thread
import time
def foo():
    print(123)
    time.sleep(1)
    print("end123")

def bar():
    print(456)
    time.sleep(3)
    print("end456")

if __name__ == '__main__':
    p1=Process(target=foo)
    p2=Process(target=bar)

    p1.daemon=True
    # p2.daemon=True
    p1.start()
    p2.start()
    print("main-------")