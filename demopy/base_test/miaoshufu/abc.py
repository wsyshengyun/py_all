# coding:utf 8


'''
练习描述符
'''


class Desc:
    def __init__(self, name):
        print('at Desc __init__ ')
        self.name = name

    def __get__(self, cls, instance):
        print('at Desc __get__ ')
        return self.name

    def __set__(self, instance, value):
        print('at Desc __get__ ')


class FuGai:
    def __init__(self, name):
        print('at FuGai __init__')
        self.name = name

    def __get__(self, cls, instance):
        print('at FuGai  __get__ ')
        return self.name


#    def __set__(self, instance, value):
#        print('at FuGai __get__ ')

class TestDesc(object):
    x = Desc(10)
    fugai = FuGai('wsy')

    def __init__(self):
        self.fugai = 'nihao'
        print('at TestDesc __init__ ')
        pass

    def __getattribute__(self, item):
        print(r"at TestDesc's __getattribute__, item =={}".format(item))
        try:
            return super(TestDesc, self).__getattribute__(item)
        except KeyError:
            return "default"
        except AttributeError as ex:
            print(ex)


obj = TestDesc()
print('*' * 50)
print(obj.x)
print('*' * 50)
print(obj.fugai)
print('*' * 50)
print(TestDesc.x)
