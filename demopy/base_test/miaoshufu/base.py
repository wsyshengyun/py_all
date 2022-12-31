# coding: utf-8
""" 
这是一个很有吸引力的模式——我们可以自定义回调函数用来响应一个类中的状态变化，
而且完全无需修改这个类的代码。这样做可真是替人分忧解难呀。现在，我们所要做的就是调用
ba.balance.add_callback(ba, low_balance_warning)，以使得每次balance变化时
low_balance_warning都会被调用。
但是我们是如何做到的呢？当我们试图访问它们时，描述符总是会调用__get__。
就好像add_callback方法是无法触及的一样！其实关键在于利用了一种特殊的情况，即，当从类的层次访问时，__get__方法的第一个参数是None
 """

from weakref import WeakKeyDictionary


class CallbackProperty(object):
    """A property that will alert observers when upon updates"""

    def __init__(self, default=None):
        self.data = WeakKeyDictionary()
        self.default = default
        self.callbacks = WeakKeyDictionary()

    def __get__(self, instance, owner):
        return self.data.get(instance, self.default)

    def __set__(self, instance, value):
        for callback in self.callbacks.get(instance, []):
            # alert callback function of new value
            callback(value)
        self.data[instance] = value

    def add_callback(self, instance, callback):
        """Add a new function to call everytime the descriptor updates"""
        # but how do we get here?!?!
        if instance not in self.callbacks:
            self.callbacks[instance] = []
        self.callbacks[instance].append(callback)


class BankAccount(object):
    balance = CallbackProperty(0)


def low_balance_warning(value):
    if value < 100:
        print("You are poor")


ba = BankAccount()
BankAccount.balance.add_callback(ba, low_balance_warning)

ba.balance = 5000
print("Balance is %s" % ba.balance)
ba.balance = 99
print("Balance is %s" % ba.balance)
# Balance is 5000
# Balance is 99
