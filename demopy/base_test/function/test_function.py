import unittest

"""
    命   名   空   间
变量存储的位置,每一个变量都需要存储到指定的命名空间中;
每一个作用域都会有一个它对应的命名空间;
全局命名空间:保存全局变量
函数命名空间:保存函数中得变量;
命名空间实际上就是一个字典,一个专门用来存储变量的字典;
locals() 获取当前作用域的命名空间,返回一个字典
globals() 可用来在任意位置获取全局命名空间;

    作   用   域
全局作用域
函数作用域
变量的查找
优先当前作用域中寻找变量,如果没有则继续上一级作用域中,直到全局作用域中,依然没有,则抛出异常
    变   量
任何变量都有特定的作用域
函数中定义的变量一般都只能在函数内使用; 这些只能在程序中特定部分使用的变量我们称为局部变量



函数参数的一些分类
1, 必须参数 
2, 关键字参数
3,  默认参数
4, 可变参数
5, 关键字可变参数
6, 强位置参数 python3.8增加的


必须参数 
    函数调用时必须传入的参数
关键字参数
    函数调用的时候,使用关键字参数,实际参数顺序可以与形式参数顺序不一致,所有的参数必须被赋值
    
默认参数(缺省参数)
    函数定义的时候,必须参数必须放置在默认参数的左侧.
    如果否
    则必须参数
可变参数(不定长参数)
关键字可变参数
    使用**形式
    关键字可变参数为字典类型
    属于可选参数
强位置参数
    / 用来知名参数形式不许使用指定位置参数,不能使用关键字参数.
    


    函   数
1 匿名函数
2 高阶函数

    匿   名   函   数
Python中用lambda来创建匿名函数
主体是一个表达式,而不是一个代码块





实参 - 实际参数
形参
    指定了形参,就必须传递几个实参
位置参数
实参的传递方式:
    1 位置参数 2 关键字参数
    位置参数:根据形参的位置传递参数
    关键字参数:根据参数的名字取传递参数
"""


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_1(self):
        pass

    def test_2(self):
        def f(c, a=1, b=1):
            return a, b, c

        # 不带默认值的参数,放在前面
        a, b, c = f(1, 2, 3)
        self.assertEqual(a, 2)
        self.assertEqual(b, 3)
        self.assertEqual(c, 1)

        # 第一个参数也可以用关键字形式传参
        x, y, z = f(c=10, a=20, b=30)
        self.assertEqual(x, 20)
        self.assertEqual(y, 30)
        self.assertEqual(z, 10)

        def f(a, b, c):
            return a, b, c

        x, y, z = f(b=1, a=2, c=3)
        self.assertEqual(x, 2)
        self.assertEqual(y, 1)
        self.assertEqual(z, 3)

        # 带星参数 * ,只能有一个
        # 也叫可变参数, 也叫位置参数
        def f(*nums):
            result = 0
            for a in nums: result += a
            return result

        self.assertEqual(f(1, 2, 3), 6)

        # 所有位置都给a,  b c 必须使用关键字参数
        def f(*a, b, c):
            return a, b, c

        # a, b, c = f(1, 3, 4, 5, 6)  !!!报错
        a, b, c = f(1, 2, 3, b=4, c=5)
        self.assertEqual(a, (1, 2, 3))
        self.assertEqual(c, c)

        # **形参,关键字参数,必须放在后面, 只能有一个
        def f(**a):
            return a

        a = f(a=1, b=2, c=3)
        self.assertEqual(a, {'a': 1, 'b': 2, 'c': 3})

        # 解包
        def f(a, b, c):
            return a, b, c

        t = 1, 2, 3
        a, b, c = f(*t)
        self.assertEqual(a, 1)
        self.assertEqual(b, 2)
        self.assertEqual(c, 3)

        d = {'a': 1, 'b': 2, 'c': 3}
        # ** 对一个字典进行解包
        a, b, c = f(**d)
        self.assertEqual(a, 1)
        self.assertEqual(b, 2)
        self.assertEqual(c, 3)

    def test_3(self):
        def f():
            pass

        self.assertEqual(f(), None)

        def f():
            return

        self.assertEqual(f(), None)

    def test_4(self):
        pass

    def test_5(self):
        pass

    def test_6(self):
        pass

    def test_7(self):
        pass

    def test_8(self):
        pass

    def test_9(self):
        pass

    def test_10(self):
        pass

    def test_11(self):
        pass

    def test_12(self):
        pass


if __name__ == '__main__':
    unittest.main()
