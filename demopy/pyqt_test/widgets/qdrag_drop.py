# -*- coding: utf-8 -*-
'''
@File    :   qdrag_drop.py
@Time    :   2022/03/19 16:32:08

'''

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit


class Button(QPushButton):
    def __init__(self, title, parent):
        super(Button, self).__init__(title, parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        self.setText(e.mimeData().text())


class MyClass(QWidget):
    def __init__(self):
        super(MyClass, self).__init__()
        self.initUI()

    def initUI(self):
        edit = QLineEdit('', self)
        edit.setDragEnabled(True)
        edit.move(30, 65)

        button = Button('Button', self)
        button.move(190, 105)

        self.setGeometry(0, 0, 500, 200)

        pass


def main():
    import sys
    app = QApplication(sys.argv)
    win = MyClass()
    win.show()
    sys.exit(app.exec_())
