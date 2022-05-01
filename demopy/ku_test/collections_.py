# coding:utf8

from collections import namedtuple

User = namedtuple('User', ['name', 'sex', 'age'])
user = User(name='kongxx', sex='male', age=21)

user1 = User._make(['kongxx', 'male', 21])

print(user)
print(user1)

print(user.name, user.sex, user.age)

user = user._replace(age=22)
print(user)

print(user._asdict())


class A:
    def __init__(self, a =2):
        """ """
        self.a = a
        self.b = 10

    def get(self):
        print('self id is {}'.format(id(self)))
        return self

    def is_in_self(self):
        print('a is in self: {}'.format('a' in self))

obj = A()
print('-'*30)
# value = obj.get()
# print("obj`s id is {}".format(id(obj)))
# print('type(self) is {}'.format(value))
# print('self is {}'.format(value))
obj.is_in_self()


