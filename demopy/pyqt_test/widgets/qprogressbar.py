# -*- coding: utf-8 -*-
'''
@File    :   qprogressbar.py
@Time    :   2022/03/19 15:16:12

'''

from ...logger.log import logger
from PyQt5.QtWidgets import QWidget, QApplication, QProgressBar, QPushButton
from PyQt5.QtCore import QBasicTimer
import time 


class MyClass(QWidget):
    def __init__(self):
        super(MyClass, self).__init__()
        self.initUI()


    def initUI(self):
        self.btn = QPushButton( 'Start', self) 
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 400, 25)

        self.timer = QBasicTimer()
        self.step = 0
        
        self.setGeometry(0, 0, 600, 400)
        self.setWindowTitle('QProgressBar')
        pass

    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Star')
        else:
            self.timer.start(50, self)
            self.btn.setText('Stop')
            self.t0 = time.time()
            logger.info("开始时间为 self.t0 = {}".format(self.t0))
        pass
    
    def timerEvent(self, e):
        """ 1到100大概运行时间为11秒,大约就是1S跑10个数字了,也就是一个数字为0.1秒 = 100毫秒 
            定时器的名称  QBasicTimer  basic:基础的
            方法有: is_Active()  
                    stop() 
                    start(100, self)  100指的是100毫秒,为定时器的间隔时间,到时间激活一下事件
        """
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText("Finished")
            logger.info("timerEvent=>stop!, run time is {} 秒".format(time.time() - self.t0))
            return 
        
        self.step += 1 
        self.pbar.setValue(self.step)
        logger.info("self.step = {}".format(self.step))
        pass
    
    
    
def main():
    import sys
    app = QApplication(sys.argv)
    win = MyClass()
    win.show()
    sys.exit(app.exec_())