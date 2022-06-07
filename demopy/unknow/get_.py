# coding:utf8
"""
target: __get__
???什么时候调用__get__, 难道只有当用作描述符的时候吗？
english
practise : 练习， 实践
failure : 失败
"""
class ClassA:
    def __init__(self, b=4):
        """ """
        self.b = b

    def __get__(self, instance, owner):
        """
        >>> obj = ClassA()
        >>> obj.a = 2  # 并不会打印__get__
        >>> obj.a  # 并不会打印__get__

        """
        print('__get__')
        pass


if __name__ == '__main__':
    # obj = ClassA()
    # obj.a = 2  # 并不会打印__get__
    # print(obj.a)  # 并不会打印__get__
    # print(obj.b)  # 并不会打印__get__
    # # print(obj.c)
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)
