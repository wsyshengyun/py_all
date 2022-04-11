# coding:utf-8


import unittest


class MyTest(unittest.TestCase):

    def setUp(self):

        pass

    def tearDown(self):

        pass

    def test1_all(self):

        L = [3, 11, 22, 11]
        side = L[0]
        result = all(x == side for x in L[1:])
        self.assertEqual(result, False)
        self.assertEqual(all([0, 1, 1]), False)
        self.assertEqual(all([1, 1, 1]), True)

        pass

    def test2_forelse(self):
        """
        for ...else...
        1 如果for中有break语句,未正常循环完毕而break跳出,那么else不会执行
        2,return同理
        3 正常执行完毕,则执行else语句
        :return:
        """

        for i in range(5):
            print(i)
        else:
            print('Hello')

    def test3_all_any(self):
        ite = (i for i in [1, 2, 3, 0, 8])
        print(type(ite))
        print(all(ite))  # False
        print(any(ite))  # True

    def test4_class(self):
        class A:
            pass

        obj = A()

        print(type(obj))
        print(type(A) is type)  # True

    def test5_class_dict(self):
        class A:
            a = 1
            pass

        obj = A()
        obj.b = 2
        self.assertTrue('b' in obj.__dict__)
        obj.__dict__['c'] = 3
        self.assertEqual(obj.c, 3)
        print('ok')
