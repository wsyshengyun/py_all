# -*- coding: utf-8 -*-
'''
@File    :   qt_base.py
@Time    :   2022/03/17 15:53:56

'''

import sys 
from PyQt5.QtWidgets import QWidget, QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(300, 150)
    w.move(300, 300)
    w.setWindowTitle('第一个基于PyQt5的桌面应用')
    w.show()
    # 进入程序主循环，并通过exit函数确保主函数完全结束； 
    sys.exit(app.exec_())
    pass