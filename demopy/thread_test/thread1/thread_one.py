# -*- coding: utf-8 -*-
'''
@File    :   thread_one.py
@Time    :   2020/09/23 17:31:32
'''


# -*- coding: UTF-8 -*-

import queue
import threading
import time
from ...logger.log import logger

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        logger.info("%s is run " % self.name)
        process_data(self.name, self.q)
        logger.info("%s is end" % self.name)

def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            logger.info("线程名字：%s ,put data =  %s" % (threadName, data))
        else:
            queueLock.release()
        time.sleep(1)

threadList = ["T1", "T2", "T3"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)

# 创建新线程
threads = []
threadID = 1
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# 填充队列
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
    logger.info("{} is ==> queue".format(word))
queueLock.release()

# 等待队列清空
while not workQueue.empty():
    pass

# 通知线程是时候退出
exitFlag = 1

# 等待所有线程完成
for t in threads:
    t.join()
logger.info ("main threading is end——")