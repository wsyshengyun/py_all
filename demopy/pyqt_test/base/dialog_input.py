# -*- coding: utf-8 -*-
'''
@File    :   dialog_input.py
@Time    :   2022/03/19 07:47:25

'''

import sys

from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
                             QInputDialog, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(130, 22)

        self.setGeometry(300, 300, 450, 350)
        self.setWindowTitle('Input dialog')
        self.show()

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')
        # QInputDialog.getText(self, 对话框标题, 标签控件内容:提示输入的东西))

        if ok:
            self.le.setText(str(text))


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
