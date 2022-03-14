import sys 
print(sys.modules.get('A.b', None))
print(sys.modules.get('A.a', None))
print("b module start")
from A import a
def foo(name):
    print("foo() function: {}".format(name))
    return 2

app = foo
# a.foo_a()
print("b module end")