# -*- coding: utf-8 -*-
'''
@File    :   multiProcessing1.py
@Time    :   2020/09/23 22:00:28
'''
""" 
python 多进程学习  
建立一个简单的进程
 """
import multiprocessing 
import time 

def process(num):
    time.sleep(num)
    print("Process ", num)


def main():
    for i in range(5):
        p = multiprocessing.Process(target=process, args=(i,))
        p.start() 

    print("Cpu numeer: " + str(multiprocessing.cpu_count()))
    for p in multiprocessing.active_children():
        print("Child process name: " + p.name + ' id ' + str(p.pid))
    print("Process Ended")

if __name__ == '__main__':
    main()
    # 你好