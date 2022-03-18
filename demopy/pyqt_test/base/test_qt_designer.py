# -*- coding: utf-8 -*-
'''
@File    :   test_q.py
@Time    :   2022/03/17 10:48:38

'''

from PyQt5.QtWidgets import QWidget, QApplication, QDialog
# from ui import Ui_test
from ui.Ui_test import Ui_Dialog
import sys 


# class MyWindow(QWidget()):
#     def __init__(self):
#         super(MyWindow, self).__init__()
#         self.new = Ui_test.Ui_Dialog()
#         self.new.setupUi(self)
#         pass

# def test():
#     app = QtWidgets.QApplication(sys.argv)
#     myshow = MyWindow()
# #     myshow.show()
#     sys.exit(app.exec_())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(dialog)
    # dialog = QWidget()
    # dialog.resize(800, 600)
    dialog.show()
    sys.exit(app.exec_())
    pass