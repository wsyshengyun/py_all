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

    # 你好我是注释
    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()
        
        openfile = QAction(QIcon('open.png'), 'Open', self)
        openfile.setShortcut('Ctrl+O')
        openfile.setStatusTip('Open new File')
        openfile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        # fileMenu.addAction(icon, text, slot)
        fileMenu.addAction(openfile)
        logger.info("menubar = {}".format(menubar))
        logger.info("fileMenu = {}".format(fileMenu))

        self.setGeometry(300, 300, 500, 450)
        self.setWindowTitle( 'File dialog')
        self.show()

    def showDialog(self):
        home_dir = str(Path.home())
            # home_dir: c:/Users/w3986
        logger.info("home_dir = {}".format(home_dir))
        # fname = QFileDialog()
        fname = QFileDialog.getOpenFileName(self, 'Open file', home_dir ) 
            # 'Open file'为对话框标题
            # fname: 为一个元组, 2个元素,1:所选择的文件的完整路径; 2:选择的范围(文件类型)[All Files(*)])
            # 当点击对话框<取消>是返回一个空的元组("", ""))
        logger.info("fname = {}".format(fname))

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()  #TODO 当有中文的时候会报错  
                self.textEdit.setText(data)

        pass
    
    
def main():
    import sys
    app = QApplication(sys.argv)
    win = Example()
    
    sys.exit(app.exec_())
