# -*- coding: utf-8 -*-
'''
@File    :   1.py
@Time    :   2021/10/01 19:39:59
'''

import threading

import time 
from ..logger.log import logger

logger.info(__name__)

def pring_age(who, age):
    print("hello every one")
    time.sleep(1)
    print("{} age is {}\n".format(who, age)) 

def print_run(who):
    print("{} is run...".format(who))
    time.sleep(3)

class Mythread(threading.Thread):
    def __init__(self, who):
        super().__init__()
        self.name = who

    def run(self) -> None:
        print("{} is runing...\n".format(self.name))
        time.sleep(3)

def main_class():
    th_obj1 = Mythread('wsy')
    th_obj2 = Mythread('lrf')
    th_obj3 = Mythread('wlh')
    th_obj1.start()
    th_obj2.start()
    th_obj3.start()
    print("over.....\n")

    pass
def main():
    t1 = time.time()
    th1 = threading.Thread(target=pring_age, args=('jet', 18))
    th2 = threading.Thread(target=pring_age, args=('jack', 19))
    th3 = threading.Thread(target=pring_age, args=('mook', 28))
    th1.start()
    th2.start()
    th3.start()
    print("times is {}".format(time.time() - t1))
    pass

def main_print_run():
    print_run('wsy')
    print_run('lrf')
    print_run('wlh')
    pass
main_print_run()