# -*- coding: utf-8 -*-
'''
@File    :   thread_queue.py
@Time    :   2020/09/23 20:27:57
'''

import queue
import threading
import time   

exitFlag = 0

class myThread(threading.Thread):
    def __init__(self, threadId, name, q):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.q = q


    def run(self):
        print("starting " + self.name)
        process_data(self.name)
        print("exiting " + self.name)


def process_data(thradName):
    while not exitFlag:
        queueLock.acquire() 
        if not workQueue.empty():
            data = workQueue.get()
            queueLock.release()
            print("%s processing %s" % (thradName, data))
        else:
            queueLock.release()
        time.sleep(1)  

threadList = ['Thread-1', 'Thread-2','Thread-3' ]
nameList = ['One', 'Two', 'Three', 'Four', 'Five']
queueLock = threading.Lock() 
workQueue = queue.Queue(10) 
threads = []
threadId = 1
# 创建新线程
for tName in threadList:
    thread = myThread(threadId, tName, workQueue)
    threads.append(thread)
    threadId += 1
# 填充队列
queueLock.acquire() 
print("Queue in....")
for word in nameList:
    workQueue.put(word)
queueLock.release()
print("Queue out....")


def main():
    global exitFlag
    # 开启线程
    for t in threads:
        t.start() 

    # 等待队列清空
    while not workQueue.empty():
        pass

    exitFlag = 1 
    print("t.join....")
    for t in threads:
        t.join() 
    print("Exiting Main Thread")

if __name__ == '__main__':
    main()
    




            