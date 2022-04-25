import unittest

from project.module.log import logger


def generator_fun():
    a = 0
    for i in range(20):
        yield a
        a += i


class MyTest(unittest.TestCase):

    def setUp(self) -> None:
        logger.info("setUp")

        pass

    def tearDown(self):
        logger.info("tearDown")
        pass

    def test_generator(self):
        g = (x * 2 for x in range(5))

    def test_generator1(self):
        """ 生成器测试 """
        g = generator_fun()
        self.assertEqual(next(g), 0)
        self.assertEqual(next(g), 0)
        self.assertEqual(next(g), 1)
        self.assertEqual(next(g), 3)
        self.assertEqual(g.__next__(), 6)
        self.assertEqual(len([i for i in g]), 15)
        pass

    def test_dict(self):
        """ 字典 """
        D = {'a': 1, 'b': 2, 'c': 3}
        # dict.setdefault(key, value)
        D.setdefault('e')
        D.setdefault('f', 9)
        D.setdefault('b', 12)

        self.assertEqual(D['e'], None)
        self.assertEqual(D.get('f'), 9)
        self.assertEqual(D.get('b'), 2)  # !!! not 12
        self.assertEqual(D.get('g'), None)  # None 不存在的值
