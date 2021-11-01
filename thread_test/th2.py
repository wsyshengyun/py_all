# -*- coding: utf-8 -*-
'''
@File    :   th2.py
@Time    :   2021/10/01 23:09:27

线程的基本应用；
Lock线程锁
Queue安全的线程队列
'''

import threading,time 

class BaseThread(threading.Thread):
    def __init__(self, threadId, threadName, lock=None):
        super().__init__()
        self.id = threadId
        self.name = threadName
        self.lock = lock

    def run(self) -> None:
        print("Thread Start: {}\n".format(self.name))
        if  self.lock: 
            print("lock...")
            self.lock.acquire()
        self.run_func()
        if  self.lock: 
            print("unlock...")
            self.lock.release()
        print("Thread Exit: {}\n".format(self.name))
    
    def run_func(self):
        pass

class MyThread(BaseThread):
    def __init__(self, threadId,  name, counter, lock=None):
        super().__init__(threadId, name, lock)
        self.counter = counter 


    def run_func(self):
        print_time(self.name, self.counter, 5)


def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("{} : {}".format(threadName, time.ctime()))
        counter -= 1


# main threading
def main():
    # 创建线程
    thread1 = MyThread(1001, 'Thread-1', 1)
    thread2 = MyThread(1002, 'Thread-2', 2) 
    print("Thread-1 is Active?", thread1.isAlive())
    thread1.start()
    thread2.start()
    print("Thread-1 is Active?", thread1.isAlive())
    thread1.join()
    thread2.join()
    print("Thread-1 is Active?", thread1.isAlive())
    print("exit")

# -----------------------------------------------------------
# 线程同步：Lock
# -----------------------------------------------------------
thread_lock = threading.Lock()
thread_list = []

class SyncThread(MyThread):
    def __init__(self, threadId, name, counter, lock):
        super().__init__(threadId, name, counter, lock)
    
    # def run(self) -> None:
    #     print("Thread Start: {}".format(self.name))
    #     thread_lock.acquire()
    #     print_time(self.name, self.counter, 5)
    #     thread_lock.release()
    #     print("Thrad Exit: {}".format(self.name))
    
    # def run_func(self):
        # thread_lock.acquire()
        # print_time(self.name, self.counter, 5)
        # thread_lock.release()

def main_sync():
    thread1 = SyncThread(1001, 'Thread-1', 1, thread_lock)
    thread2 = SyncThread(1001, 'Thread-2', 2, thread_lock)
    thread_list.append(thread1)
    thread_list.append(thread2)
    for th in thread_list:
        th.start()
    for th in thread_list:
        th.join() 
    print("exit!!")
    pass

# -----------------------------------------------------------
# queue
# -----------------------------------------------------------
import queue
exitFlag = 0
queueLock = threading.Lock()
# 创建队列
work_queue  = queue.Queue(10)

class QueueThread(BaseThread):
    def __init__(self, threadId, threadName, q:queue.Queue):
        super().__init__(threadId, threadName)
        self.q  = q

    # def run(self) -> None:
    #     print("Start {}".format(self.name))
    #     process_data(self.name, self.q)
    #     print("Exit {}".format(self.name))

    def run_func(self):
        process_data(self.name, self.q)


def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not q.empty():
            data = q.get()
            print("{} processing - {}".format(threadName, data))
            queueLock.release()
        else:
            queueLock.release()
        time.sleep(1)
    # else:
    #     print("quit while!!")


def get_thread_message():
    print("-----------------------------------------------")
    print("当前的线程为：{}".format( threading.current_thread())) # 输出线程对象 = 主线程对象
    print("当前的线程为：{}".format( threading.get_ident())) # 输出线程号码
    print("当前活跃的线程为:{}".format(threading.active_count()))# 4
    print("当前活动的Thread对象列表：{}".format(threading.enumerate()))# 4个线程对象 1主3子线程
    print("返回主Thread对象：{}".format(threading.main_thread()))  # 主线程对象
    print("允许的最大超时时间：{}".format(threading.TIMEOUT_MAX)) # 大约为50天
    # print("{}".format())
    print("-----------------------------------------------")


# 
def main_queue():
    global exitFlag
    thread_id = 1 
    name_list = ['one', 'two', 'three', 'four', 'five']
    threads = []
    thread_list = ['Thread-1', 'Thread-2', 'Thread-3']

    # create new thread 
    for t_name in thread_list:
        th = QueueThread(thread_id, t_name, work_queue)
        th.start()
        threads.append(th)
        thread_id += 1
        # 

    get_thread_message()

    # for t in threads:
    #     print("join")
    #     t.join()

    # insert queue  
    queueLock.acquire()
    print("填充队列中>>>>>>>>>>>>>>>>>\n")
    for name in name_list:
        work_queue.put(name)
    print("填充队列完毕>>>>>>>>>>>>>>>>>\n")
    queueLock.release()

    # wait queue empty
    while not work_queue.empty():
        pass

    # 
    exitFlag = 1 

    # 
    for t in threads:
        t.join()

    # 
    print("exit")

    pass




# -----------------------------------------------------------
# run 
# -----------------------------------------------------------
main_queue()

       