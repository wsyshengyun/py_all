# -*- coding: utf-8 -*-
'''
@File    :   dialog_file.py
@Time    :   2022/03/19 00:13:55

'''
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QTextEdit, \
    QAction, QFileDialog 
from PyQt5.QtGui import QIcon
from ...logger.log import logger

from pathlib import Path

class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()


    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()
        
        openfile = QAction(QIcon('open.png'), 'Open', self)
        openfile.setShortcut('Ctrl+O')
        openfile.setStatusTip('Open new File')
        openfile.triggered.connect(self.showDialog)
        self.show()

    def showDialog(self):
        pass
    
    
def main():
    import sys
    app = QApplication(sys.argv)
    win = Example()
    
    sys.exit(app.exec_())
