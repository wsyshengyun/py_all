# -*- coding: utf-8 -*-
'''
@File    :   test_boundedSemaphore.py
@Time    :   2022/03/16 15:15:57

'''


import threading
import time
from ...logger.log import logger


def run(n, semaphore):
    semaphore.acquire()
    time.sleep(1)
    logger.info("run the thread: {}".format(n))
    semaphore.release()   # 释放
    
def test_run():
    """ 
    使用时间是5秒
    """
    t0 = time.time()
    num = 0
    semaphore = threading.BoundedSemaphore(5)
    for i in range(22):
        t = threading.Thread(target=run, args=('T%s'%i, semaphore))
        t.start()
    
    while threading.active_count() != 1: 
        pass
    else:
        logger.info("___________all threads done___________")
    logger.info("times is {}".format(time.time() - t0))

test_run()
