# -*- coding: utf-8 -*-
'''
@File    :   unit.py
@Time    :   2021/11/14 12:51:44

'''
import unittest 
from mydict import Dict 

class TestDict(unittest.TestCase):
    """ 这是一个测试类，从unittest.TestCase继承
    下面以test开关的就是测试方法； 不以test开头的不会被执行；
     """
    
    def setUp(self) -> None:
        """ 可以在单元测试中编写两个特殊的setUp()和tearDown()方法。这两个方法会分别在每调用一个测试方法的前后分别被执行。 """
        print("setUp...") 
        self.dict = Dict()
        # return super().setUp()

    def tearDown(self) -> None:
        print('tearDown...')
        # return super().tearDown()
    
    def test_init(self):
        # self.dict = Dict(a=1, b='test')
        self.dict.update({'a':1, 'b':'test'})
        self.assertEqual(self.dict.a, 1)
        self.assertEqual(self.dict.b, 'test')
        self.assertTrue(isinstance(self.dict, dict))
    
    def test_key(self):
        self.dict['key'] = 'value'
        self.assertEqual(self.dict.key, 'value')
    
    def test_attr(self):
        self.dict.key = 'value'
        self.assertTrue('key' in self.dict)
        self.assertEqual(self.dict['key'], 'value')
    
    def test_keyerror(self):
        with self.assertRaises(KeyError):
            value = self.dict['empty']
    
    def test_attrerror(self):
        with self.assertRaises(AttributeError):
            value = self.dict.empty

        
if __name__ == '__main__':
    """ 运行单元测试
    另一种运行方法是在命令行：python unittest -m 文件名
     """
    unittest.main()
    pass