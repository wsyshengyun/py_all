# from packb.moduleb1 import b1
# from ..moduleb1 import b1
from .. import b1
print("in modulec1.py")


c1 = 100

def modulec1_fun():
    print("in modulec1_fun")

print("in module c1, b1 value is: %s" %b1)