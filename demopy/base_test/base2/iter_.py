# coding:utf8
# from collections import Iterator   # collections在python3.9已经停止使用了


def test1():
    class A(object):
        def __init__(self, a=2):
            """ """
            self.a = a
            self.lit = []
            self.o = {}
            self.i = 0

        def __iter__(self):
            print("__iter__")
            return iter(self.o)

    obj = A()
    obj.lit = [1, 2, 3, 4, 5, 6]
    ltt = [3, 4, 5, 6, 7]
    dit = {'a': 1, 'b': 2, 'c': 3}
    obj.o = dit
    it = iter(obj)
    # it = obj.__iter__()
    # for k, v in it:
    #     print(k, v)
    print(next(it))
    print(next(it))
    print(next(it))


# test1()


def test2():
    class B(object):
        a = 0

        def __iter__(self):
            print("__iter__")
            return self

        def __next__(self):
            self.a += 1
            if self.a > 5:
                raise StopIteration
            return 1

    obj = B()
    # 生成一个迭代器
    it = iter(obj)    # 打印__iter__
    # 再次生成一个迭代器
    for i in obj:  # 打印__iter__
        print(i)
    pass


test2()




