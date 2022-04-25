# -*- coding: utf-8 -*-
'''
@File    :   qpushbutton.py
@Time    :   2022/03/19 10:40:13

'''
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QFrame


class MyClass(QWidget):
    def __init__(self):
        super(MyClass, self).__init__()
        self.initUI()

    def initUI(self):
        self.col = QColor(0, 0, 0)

        redb = QPushButton('Red', self)
        redb.setCheckable(True)
        redb.move(20, 20)
        redb.clicked[bool].connect(self.setColor)

        greenb = QPushButton('Green', self)
        greenb.setCheckable(True)
        greenb.move(20, 90)
        greenb.clicked[bool].connect(self.setColor)

        blueb = QPushButton('Blue', self)
        blueb.setCheckable(True)
        blueb.move(20, 160)
        blueb.clicked[bool].connect(self.setColor)

        self.square = QFrame(self)
        self.square.setGeometry(350, 20, 100, 100)
        self.square.setStyleSheet("QWidget { background-color: %s}" %
                                  self.col.name())
        # self.square.setStyleSheet( "QWidget { background-color: {}}".format( 
        #   self.col.name()))

        # self.setGeometry(300, 300, 600, 300)

        pass

    def setColor(self, pressed):
        source = self.sender()
        if pressed:
            val = 255
        else:
            val = 0

        if source.text() == 'Red':
            # self.col.setRed(val)
            self.col.setRgb(255, 0, 0)
        elif source.text() == 'Green':
            self.col.setGreen(val)
            self.col.setRgb(0, 255, 0)
        else:
            # self.col.setBlue(val)
            self.col.setRgb(0, 0, 255)

        self.square.setStyleSheet("QWidget { background-color: %s}" %
                                  self.col.name())


def main():
    import sys
    app = QApplication(sys.argv)
    win = MyClass()
    win.show()
    sys.exit(app.exec_())
