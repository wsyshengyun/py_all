# -*- coding: utf-8 -*-
'''
@File    :   qcheckbox.py
@Time    :   2022/03/19 09:51:36

'''

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QCheckBox

from ...logger.log import logger


class MyClass(QWidget):
    def __init__(self):
        super(MyClass, self).__init__()
        self.initUI()

    def initUI(self):
        cb = QCheckBox('Show title', self)  # self
        cb.move(20, 20)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)

        self.setGeometry(700, 400, 750, 350)
        self.setWindowTitle('QcheckBox')

        pass

    def changeTitle(self, state):
        logger.info("state={}".format(state))
        logger.info("Qt.Checked = {}".format(Qt.Checked))
        if state == Qt.Checked:
            self.setWindowTitle('Qcheckbox')
        else:
            self.setWindowTitle('')
        pass


def main():
    import sys
    app = QApplication(sys.argv)
    win = MyClass()
    win.show()
    sys.exit(app.exec_())
