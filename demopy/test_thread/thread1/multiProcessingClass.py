# -*- coding: utf-8 -*-
'''
@File    :   multiProcessingClass.py
@Time    :   2020/09/23 22:07:02
'''

""" 
python 进程的学习  
通过类建立进程
 """

from multiprocessing import Process, Lock
import time 



class MyProcess(Process):
    def __init__(self, loop, lock):
        Process.__init__(self)
        self.loop = loop
        pass



    def run(self):
        for count in range(self.loop):
            time.sleep(0.1)
            print("Pid: `                " + str(self.pid) + ' LoopCount: ' + str(count)) 

def main():
    for i in range(10, 20):
        p = MyProcess(i) 
        # p.daemon = True 
        p.start() 
        # p.join()


if __name__ == '__main__':
    main()
    print("nihaoa")
    
