import unittest

"""
1、字符串前加 u

例：u"我是含有中文字符组成的字符串。"

作用：

后面字符串以 Unicode 格式 进行编码，一般用在中文字符串前面，防止因为源码储存格式问题，导致再次使用时出现乱码。

2、字符串前加 r

例：r"\n\n\n\n”　　表示一个普通生字符串 \n\n\n\n，而不表示换行了。

作用：

去掉反斜杠的转移机制。

(特殊字符：即那些，反斜杠加上对应字母，表示对应的特殊含义的，比如最常见的”\n”表示换行，”\t”表示Tab等。 )

应用：

常用于正则表达式，对应着re模块。

3、字符串前加 b

例: response = b'Hello World!' b' ' 表示这是一个 bytes 对象

作用：

b" "前缀表示：后面字符串是bytes 类型。

用处：

网络编程中，服务器和浏览器只认bytes 类型数据。

如：send 函数的参数和 recv 函数的返回值都是 bytes 类型

附：

在 Python3 中，bytes 和 str 的互相转换方式是

str.encode(‘utf-8')

bytes.decode(‘utf-8')

4、字符串前加 f

import time

t0 = time.time()

time.sleep(1)

name = ‘processing'

以 f开头表示在字符串内支持大括号内的python 表达式

print(f'{name} done in {time.time() - t0:.2f} s')

输出：

processing done in 1.00 s


"""


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
        while x < 100:
            x += 1
        else:
            # 如果没有遇到break就会执行这里
            print('nihao')

    def test_6(self):
        a, b, *other = 1, 2, 3, 4, 5, 6
        self.assertEqual(a, 1)
        self.assertEqual(b, 2)

        a, *other, b = 1, 2, 3, 4, 5, 6
        self.assertEqual(b, 6)

        # uppacking操作也可以用在迭代器上,但是没有优势
        def generate_csv():
            for i in range(1, 7):
                yield i
            # yield (1, 2, 3, 4, 5, 6)

        it = generate_csv()
        a, *b = it
        self.assertEqual(a, 1)

        self.assertEqual(list(range(1, 4)), [1, 2, 3])

    def test_7(self):
        pass

    def test_8(self):
        pass

    def test_9(self):
        pass


if __name__ == '__main__':
    unittest.main()
