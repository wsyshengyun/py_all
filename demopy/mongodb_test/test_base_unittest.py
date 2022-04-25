# -*- coding: utf-8 -*-
'''
@File    :   mongo_unittest.py
@Time    :   2022/03/27 20:15:07

'''

import unittest


class Test_Main(unittest.TestCase):
    """ 继承了unittest.TestCase就创建了一个测试用例 """

    i_up = 0

    # 若果要跑所有的用例,只运行一次前提条件和结束条件,则用setUpClass 和 tearDownClass
    @classmethod
    def setUpClass(cls):
        # logger.info("setUpClass")
        pass

    @classmethod
    def tearDownClass(cls):
        # logger.info("tearDownClass")
        pass

    def setUp(self):
        self.i_up += 1
        # logger.info("setUP : {}".format(self.i_up))
        pass

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
        pass

    def tearDown(self):
        # logger.info("tearDown")
        pass

    def test_isupper(self):
        self.assertTrue("FOO".isupper())
        # self.assertTrue("Foo".isupper())
        pass

    def test_isNone(self):
        a = None
        self.assertIsNone(a)
        pass

    def test_int(self):
        a = 'a'
        b = ['b', 'a', 'c']
        self.assertIn(a, b)
        pass

    def test_isInstance(self):
        obj = 5
        clsobj = int
        self.assertIsInstance(obj, clsobj)
        pass

    def test_assert(self):
        assert 11 > 10

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])

        with self.assertRaises(TypeError):
            s.split(2)
        pass

    def test_add_two_num(self):
        # logger.info("5+7")
        pass

    def test_sub_tow_num(self):
        # logger.info("5*7")

        pass
