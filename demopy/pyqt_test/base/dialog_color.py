# -*- coding: utf-8 -*-
'''
@File    :   dialog_color.py
@Time    :   2022/03/18 15:43:36

'''

import sys

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import (QWidget, QPushButton, QFrame, QColorDialog, QApplication)

from ...logger.log import logger


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        col = QColor(0, 0, 0)
        logger.info("col = {}, col.name = {}".format(col, col.name()))
        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget{ background-color:%s}"
                               % col.name())

        self.frm.setGeometry(171, 40, 200, 200)
        self.setGeometry(300, 300, 450, 350)
        self.setWindowTitle("color dialog")
        self.show()
        pass

    def showDialog(self):
        col = QColorDialog.getColor()
        logger.info("col = {}, col.name = {}".format(col, col.name()))
        logger.info("type(col) = {}".format(type(col)))

        if col.isValid():
            logger.info("col.isValid = {}".format(col.isValid()))
            self.frm.setStyleSheet("QWidget{background-color: %s}" %
                                   col.name())


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

    pass
