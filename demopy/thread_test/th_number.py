# -*- coding: utf-8 -*-
'''
@File    :   th3.py
@Time    :   2021/10/02 19:21:53
'''

import threading ,time
from ..logger.log import logger

# -----------------------------------------------------------
# 没有锁的情况下，数据可以被多个线程更改，结果不为20000了；
# -----------------------------------------------------------

number = 0 

def sub():
    global number
    num = 10
    # num = 100000
    for i in range(num):
        number += 1
        time.sleep(1)
        logger.info("子线程{}, number= {}"
          .format( threading.current_thread().getName() ,number))

th1 = threading.Thread(target=sub, name='T1')
th2 = threading.Thread(target=sub, name='T2')
th3 = threading.Thread(target=sub, name='T3')
lit = [th1, th2, th3]
for th in lit:
    th.setDaemon(True)
    th.start()
for th in lit:
    th.join()
    pass
time.sleep(4)
logger.info("number = {}".format(number))