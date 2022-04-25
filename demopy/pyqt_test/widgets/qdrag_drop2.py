# -*- coding: utf-8 -*-
'''
@File    :   qdrag_drop2.py
@Time    :   2022/03/19 17:02:18

'''

from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton

from ...logger.log import logger


class Button(QPushButton):

    def __init__(self, title, parent):
        super(Button, self).__init__(title, parent)

    def mouseMoveEvent(self, e):
        if e.buttons() != Qt.RightButton:
            return

        mimeData = QMimeData()

        drag = QDrag(self)
        drag.setMimeData(mimeData)
        pos = e.pos() - self.rect().topLeft()
        drag.setHotSpot(pos)
        logger.info("pos = {}".format(pos))

        dropAction = drag.exec_(Qt.MoveAction)
        pass

    def mousePressEvent(self, e):
        super().mousePressEvent(e)

        if e.buttons() != Qt.RightButton():
            return

            # if e.buttons() == Qt.LeftButton():
        #     return 
        #     logger.info("press, pos is {}".format(e.pos()))
        # pass


class MyClass(QWidget):

    def __init__(self):
        super(MyClass, self).__init__()
        self.initUI()

    def initUI(self):
        self.setAcceptDrops(True)

        self.button = Button('Button', self)
        self.button.move(100, 65)

        self.setGeometry(0, 0, 600, 500)
        pass

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        position = e.pos()
        self.button.move(position)

        e.setDropAction(Qt.MoveAction)
        e.accept()


def main():
    import sys
    app = QApplication(sys.argv)
    win = MyClass()
    win.show()
    sys.exit(app.exec_())
