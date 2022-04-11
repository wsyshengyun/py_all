# coding:utf8


class Borg(object):
    _share_state = {}

    def __init__(self):
        self.__dict__ = self._share_state


class IBorg(Borg):

    def __init__(self):
        Borg.__init__(self)
        self.state = 'init'
        pass


i1 = IBorg()
i2 = IBorg()
print(i1 is i2)  # False
i2.state = 'nihao'
print(i1.state)


class ABorg(Borg): pass


class BBorg(Borg): pass


class A1Borg(ABorg): pass


a = ABorg()
b = BBorg()
a1 = A1Borg()

a.x = 100
print(b.x, a1.x)  # 100, 100
