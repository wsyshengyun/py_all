import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_1(self):
        # 交换两个元素
        a, b = 1, 2
        a, b = b, a
        self.assertEqual(a, 2)
        self.assertEqual(b, 1)
        pass

    def test_2(self):
        # 逻辑判断 or and
        def f(num):
            f_return = lambda s: s
            return (num == 1 and f_return("one")) \
                   or (num == 2 and f_return('Two')) \
                   or f_return('Other')

        self.assertEqual(f(1), 'one')
        self.assertEqual(f(2), 'Two')
        self.assertEqual(f(3), "Other")

        self.assertEqual(1 and 2, 2)
        self.assertEqual(0 and 2, 0)
        self.assertEqual(1 and False and 2, False)

        self.assertEqual(1 or 2, 1)
        self.assertEqual(0 or 2, 2)
        self.assertEqual(0 or 0 or 2, 2)
        self.assertEqual(0 or 1 or 2, 1)
        self.assertEqual(1 and (6 or 8), 6)
        # 对于 or 来说, 1有短路的作用, 当遇到1的时候,不在继续后面的逻辑运算了.
        # 对于and来说, 0具有短路的作用, 当遇到0的时候,不在继续后面的操作了,否则,继续后面
        # 对于and来说, 0 没有意义; 对于or来说1没有意义.

    def test_3(self):
        # 解包
        c = (1, 3, 4)
        # a, b = *c  !!!错误 不能使用*c形式
        # a, b = c  !!!报错, c元素太多,无法解包
        c = 1, 3
        a, b = c
        self.assertEqual(a, 1)
        self.assertEqual(b, 3)

    def test_4(self):
        # ord 与 chr
        self.assertNotEqual(ord('a'), '97')
        self.assertEqual(ord('a'), 97)
        self.assertEqual(chr(97), 'a')

        #  arrert
        # assert False "False is assert"
        assert 1
        assert True

    def test_5(self):
        x = 1
        while x <= 100:
            x += 1
        self.assertEqual(x, 101)

        # for
        i = 0
        for i in range(1, 100):
            pass

        # 没有do...while
        #
        x = 0
        while x<100:
            x += 1
        else:
            # 如果没有遇到break就会执行这里
            print('nihao')


    def test_6(self):
        pass

    def test_7(self):
        pass

    def test_8(self):
        pass

    def test_9(self):
        pass


if __name__ == '__main__':
    unittest.main()
