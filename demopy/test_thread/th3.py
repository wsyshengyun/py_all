# -*- coding: utf-8 -*-
'''
@File    :   th3.py
@Time    :   2021/10/02 19:21:53
'''

# -----------------------------------------------------------
# 没有锁的情况下，数据可以被多个线程更改，结果不为20000了；
# -----------------------------------------------------------
import threading ,time

number = 0 

def sub():
    global number
    for i in range(100000):
        number += 1
    print("子线程{}结束后，number的值为： {}".format(
        threading.current_thread().getName()
        ,number
    ))

th1 = threading.Thread(target=sub)
th2 = threading.Thread(target=sub)
th1.start()
th2.start()
time.sleep(4)
print("number = {}".format(number))