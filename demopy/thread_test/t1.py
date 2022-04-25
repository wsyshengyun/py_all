# -*- coding: utf-8 -*-
'''
@File    :   1.py
@Time    :   2021/10/01 19:39:59
'''

import threading
import time

from ..logger.log import logger

logger.info("in t1.py——")


# -----------------------------------------------------------
# threading
# -----------------------------------------------------------
def pring_age(who, age):
    logger.info("hello every one")
    time.sleep(1)
    logger.info("{} age is {}\n".format(who, age))


def print_run(who):
    logger.info("{} is run...".format(who))
    time.sleep(3)


def test_threading():
    t1 = time.time()
    th1 = threading.Thread(target=pring_age, args=('jet', 18))
    th2 = threading.Thread(target=pring_age, args=('jack', 19))
    th3 = threading.Thread(target=pring_age, args=('mook', 28))
    th1.start()
    th2.start()
    th3.start()
    logger.info("times is {}".format(time.time() - t1))
    pass


# -----------------------------------------------------------
# threadind.class
# -----------------------------------------------------------
class Mythread(threading.Thread):
    ths = []

    def __init__(self, who):
        super().__init__()
        self.name = who

    def run(self) -> None:
        logger.info("{} is runing...\n".format(self.name))
        time.sleep(3)

    @classmethod
    def joins(cls):
        for th in cls.ths:
            th.join()

    @classmethod
    def starts(cls):
        for th in cls.ths:
            th.setDaemon(True)
            th.start()


def test_mythread():
    th_obj1 = Mythread('wsy')
    th_obj2 = Mythread('lrf')
    th_obj3 = Mythread('wlh')
    th_obj1.start()
    th_obj2.start()
    th_obj3.start()
    logger.info("over.....\n")


# main_print_run()

# -----------------------------------------------------------
# thread: Join
# -----------------------------------------------------------
def foo():
    # logger.info("in foo --- ")
    # logger.info("共有{}个线程在运行，当前线程的名字为{}.".format(threading.active_count(), threading.current_thread().name))
    t = time.time()
    while ((time.time() - t) < 7):
        logger.info("{} is  run...{}".format(threading.current_thread().name, threading.active_count()))
        time.sleep(1)
    # logger.info("out foo --- ")
    pass


def test_threading_join():
    logger.info("start---")
    t1 = threading.Thread(target=foo, args=(), name="T1")
    t2 = threading.Thread(target=foo, args=(), name="T2")
    t3 = threading.Thread(target=foo, args=(), name="T3")
    t4 = threading.Thread(target=foo, args=(), name="T4")
    lit = [t1, t2, t3, t4]
    for t in lit:
        t.setDaemon(True)
        t.start()
        time.sleep(4)
    for t in lit:
        t.join()
    # t.join(timeout=4)
    logger.info("main:共有{}个线程在运行，当前线程的名字为{}.".format(threading.active_count(), threading.current_thread().name))
    logger.info("end---")
    pass


test_threading_join()
