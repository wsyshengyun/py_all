﻿# from demopy.thread_test import t1
# from demopy.logger.test import test1
# from demopy.base.file.ini import ini_t
# from demopy.thread_test import t1
# from demopy.thread_test import th_number
# from demopy.thread_test.thread1 import thread_one
# from demopy.thread_test.thread_event import test_boundedSemaphore
# from demopy.thread_test.thread_event import light
# from demopy.pachong_test.selenium_test import nihao
# from demopy.pyqt_test import test_q
# from demopy.pyqt_test.base.dialog_color import main
# from demopy.pyqt_test.base.dialog_font import main
# from demopy.pyqt_test.base.dialog_file import main
# from demopy.pyqt_test.base.dialog_input import main
# from demopy.pyqt_test.base.signal_1 import main
# from demopy.pyqt_test.widgets.qcheckbox import main
# from demopy.pyqt_test.widgets.qpushbutton import main
# from demopy.pyqt_test.widgets.qslider import main
# from demopy.pyqt_test.widgets.qprogressbar import main
# from demopy.pyqt_test.widgets.qdrag_drop import main
# from demopy.pyqt_test.widgets.qdrag_drop2 import main
# from demopy.mongodb_test.mongo_unittest import main
import unittest , os 
from demopy.logger.log import logger
# main()
logger.info('-' * 100)


# from demopy.unittest_test import 

# def run_test():
    
s = unittest.TestSuite()
loader = unittest.TestLoader()

# path = 'demopy/unittest_test'
path = 'demopy/mongodb_test'
# s.addTests(loader.discover(os.getcwd()))
s.addTests(loader.discover(path))

run = unittest.TextTestRunner()
run.run(s)


# run_test()