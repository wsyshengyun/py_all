# from A.b import app
print("a module start")
from A import b

# app(__name__)
# b.app(__name__)

def foo_a():
    print("in foo_a")

print("a module end")