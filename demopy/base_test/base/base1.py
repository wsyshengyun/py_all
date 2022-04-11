class A:
    def __init__(self, a=0):
        self.a = a
        pass

    def foo(self):
        print('in A.foo')
        return self.__class__
        pass

    def foo_a(self):
        pass


class B:
    def __init__(self, b=11):
        self.b = b
        pass

    # def foo(self):
    #
    #     print('in B.foo')
    #     pass


# obj = A()
# objb = B()
# print(obj.foo())
# print(eval('A'))  # <class '__main__.A'>
#
# objb.__class__ = eval('A')
# print(objb.b, '   is objb.a')
# print(objb.foo())
# print('- ' * 30)
# print(objb.__dict__)
# print(obj.__dict__)
# print('- ' * 30)
# print(dir(objb))
# print(dir(obj))

import random


class ComputerState(object):
    name = 'state'
    next_states = []
    random_states = []

    def __init__(self):
        self.index = 0
        pass

    def __next__(self):
        if self.index < len(self.next_states):
            state = self.next_states[self.index]
            self.index += 1
            return self.set_class_from_state_name(state)
        else:
            self.index = 0
            state = random.choice(self.random_states)
            return self.set_class_from_state_name(state)
        pass

    def set(self, state):
        if self.index < len(self.next_states):
            if state in self.next_states:
                self.index = self.next_states.index(state)
                return self.set_class_from_state_name(state)
            else:
                raise Exception
        else:
            self.index = 0
            if state in self.random_states:
                return self.set_class_from_state_name(state)

    def set_class_from_state_name(self, state):
        self.__class__ = eval(state)
        return self.__class__

    def __iter__(self):
        return self
        pass

    def change(self):
        return self.__next__()
        pass

    def __str__(self):
        return


class ComputerOff(ComputerState):
    next_states = ['ComputerOn']
    random_states = ['ComputerSuspend', 'ComputerHibernate', 'ComputerOff']


class ComputerOn(ComputerState):
    random_states = ['ComputerSuspend', 'ComputerHibernate', 'ComputerOff']


class ComputerWakeUp(ComputerState):
    random_states = ['ComputerSuspend', 'ComputerHibernate', 'ComputerOff']
    pass


class ComputerSuspend(ComputerState):
    next_states = ['ComputerWakeUp']
    random_states = ['ComputerSuspend', 'ComputerHibernate', 'ComputerOff']
    pass


class ComputerHibernate(ComputerState):
    next_states = ['ComputerOn']
    random_states = ['ComputerSuspend', 'ComputerHibernate', 'ComputerOff']
    pass


class Computer(object):
    def __init__(self, module):

        self.module = module
        self.state = ComputerOff()
        pass

    def __str__(self):
        return str(self.state)

    def change(self, state=None):

        if state is None:
            return self.state.change()
        else:
            return self.state.set(state)


obj = Computer('nihao')

obj.change('ComputerOn')
obj.state.next_states.append('ComputerWakeUp')
obj.state.next_states.append('ComputerSuspend')
obj.state.next_states.append('ComputerHibernate')

for i in range(5):
    obj.state.__next__()
    print(obj.state.__class__)
