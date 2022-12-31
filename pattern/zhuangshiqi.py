# coding:utf8

from abc import ABCMeta


class Person(metaclass=ABCMeta):
    def __init__(self, name=None):
        self._name = name

    def wear(self):
        print('wear')

    def __str__(self):
        return f"<Person: {self._name}>"

    def get_name(self):
        return self._name


class Decorator(Person):
    def __init__(self, person):
        """ """
        self._decorated = person


class Decorator1(Person):
    def __init__(self, person, name=None):
        """ """
        super(Decorator1, self).__init__(name)
        self._decorated = person


if __name__ == '__main__':
    obj_person = Person("wsy")
    obj_decorator = Decorator(obj_person)
    try:
        print('1')
        print(obj_decorator.__name)
    except:
        print('2')
        print(obj_decorator._decorated)

    obj_decorator.wear()
    print('-' * 50)
    obj_decorator1 = Decorator1(obj_person, 'jbd')
    # print(obj_decorator1.__name)
    print(obj_decorator1._name)
    print(obj_decorator1.get_name())

