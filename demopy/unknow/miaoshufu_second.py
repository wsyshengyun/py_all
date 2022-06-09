# coding:utf8


class Value(object):
    def __init__(self, name=None):
        """ """
        self.name = name
        print('__int__')

    def __get__(self, instance, owner):
        print('__get__')
        pass

    def __set__(self, instance, value):
        print('__set__')
        pass


class Number:
    # v1 = Value('v1')
    v1 = Value()
    v2 = Value()

    def __init__(self, a1=0, a2=11):
        """ """
        self.v1 = a1
        self.v2 = a2

    def __str__(self):
        return  f'<Number: v1={self.v1}, v2={self.v2}'


if __name__ == '__main__':
    n = Number(1, 9)
    print(n)
    # n2 = Number(2)
