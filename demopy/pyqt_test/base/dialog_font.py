# -*- coding: utf-8 -*-
'''
@File    :   dialog_font.py
@Time    :   2022/03/18 22:45:05

'''
import sys

from PyQt5.QtWidgets import QApplication, QFontDialog, QWidget, QPushButton \
    , QSizePolicy, QLabel, QVBoxLayout

from ...logger.log import logger


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        pass

    def initUI(self):
        vbox = QVBoxLayout()
        btn = QPushButton('Dialog', self)
        btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        logger.info("QsizePolicy.Fixed={}".format(QSizePolicy.Fixed))
        btn.move(20, 20)

        vbox.addWidget(btn)

        btn.clicked.connect(self.showDialog)

        self.lbl = QLabel('knowledge only matters', self)
        self.lbl.move(130, 20)

        vbox.addWidget(self.lbl)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 450, 350)
        self.setWindowTitle('Font dialog')
        self.show()

        pass

    def showDialog(self):
        font, ok = QFontDialog.getFont()
        family, weight, bold, fams, tostr = \
            font.family(), font.weight(), font.bold(), '_', font.toString()
        logger.info("font={}, ok={}".format(font, ok))
        logger.info("family={}, weight={}, bold={}, fams={}, tostr={}".format(
            family, weight, bold, fams, tostr
        ))
        if ok:
            self.lbl.setFont(font)
        pass


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


from PyQt5.QWigets import QWidget, QApplication


class my(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        pass


class Nihao(QWidget):
    def __init__(self):
        super(Nihao, self).__init__()
        self.initUI()

    def initUI(self):
        pass
