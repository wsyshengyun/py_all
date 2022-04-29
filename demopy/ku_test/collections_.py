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

