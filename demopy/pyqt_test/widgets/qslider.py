# -*- coding: utf-8 -*-
'''
@File    :   qslider.py
@Time    :   2022/03/19 13:23:07

'''

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QSlider, QLabel


class MyClass(QWidget):
    def __init__(self):
        super(MyClass, self).__init__()
        self.initUI()

    def initUI(self):
        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30, 40, 200, 30)
        sld.valueChanged[int].connect(self.changeValue)

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('mute.png'))
        self.label.setGeometry(250, 40, 80, 30)

        self.setGeometry(300, 300, 350, 250)

    def changeValue(self, value):
        min = "C:\\Program Files\\WindowsApps\\E0469640.LenovoUtility_4.2.33.0_x64__5grkq8ppsgwt4\\skin\\IE2\\imgs\\02min.png"
        mute = "D:\\Program Files (x86)\\DingDing\\main\\current\\plugins\\tblive\\data\\obs-studio\themes\\Dark\\mute.png"
        max = "D:\\zi资料\\W.sy学习资料\\example_pyqt_anyperson\\menu\\max.png"
        med = "C:\\Program Files (x86)\\SogouInput\\Components\\SkinBox\\1.0.0.441\\icon.png"
        if value == 0:
            # self.label.setPixmap( 'mute.png')
            self.label.setPixmap(min)
        elif 0 < value < 30:
            # self.label.setPixmap( 'min.png')
            self.label.setPixmap(mute)
        elif 30 < value < 80:
            # self.label.setPixmap( 'med.png')
            self.label.setPixmap(med)
        else:
            # self.label.setPixmap( 'max.png')
            self.label.setPixmap(max)


def main():
    import sys
    app = QApplication(sys.argv)
    win = MyClass()
    win.show()
    sys.exit(app.exec_())
