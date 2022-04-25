# coding:utf8

# -----------------------------------------------------------
# 生成器的测试 
# -----------------------------------------------------------

def main_gen():
    a = (i for i in range[1, 2, 3, 4, 5, 6, 8, 7])
    print(a)
    pass


# -----------------------------------------------------------
# 迭代器
# -----------------------------------------------------------
class Feibo(object):
    def __init__(self, a=1, b=1):
        self.a = a
        self.b = b

    def __call__(self):
        self.a, self.b = self.a + self.b, self.a

    def __iter__(self):
        return self


def main_feibo():
    obj = Feibo()
    pass


# -----------------------------------------------------------
# 生成器
# -----------------------------------------------------------

def fun_gen(arg):
    for i in range(10):
        yield i + arg


def repeater(value):
    while True:
        new = (yield value)
        if new is not None:
            value = new
        # ============================================================================


def repeater2():
    count = 0
    while True:
        count += yield count


def main_gen():
    g = repeater2()
    print(g.send(None))
    print(g.send(1))
    print(g.send(1))
    print(g.send(3))
    print(g.send(1))
    pass


# main_gen()

# =================================send==========================================
def func_gen():
    value = "nk1"
    while True:
        t = yield value
        if t == 'nk':
            print("is equel")
            value = 10000


def main_func():
    g = func_gen()
    print(g.send(None))
    print(g.send('nk'))
    print(g.send("nihao"))


# main_func()
# =======================yield from =====================================================
def fun_gen_b():
    for i in range(5):
        yield i


def fun_gen_a():
    for i in range(100, 105):
        yield i


def fun_gen_combain():
    yield from fun_gen_a()
    yield from fun_gen_b()


def main_fun_gen3():
    for i in fun_gen_combain():
        print(i, end=',')


# main_fun_gen3()

# ============================================================================
def fb(n):
    a, b = 1, 1
    while (b < n):
        yield b
        a, b = b, a + b


def main_fb(n):
    k = 0
    for k, i in enumerate(fb(n)):
        print(i, end='  ')
    print()
    print(k)


# 使用普通方法实现菲薄哪切数列
def func_fb(n):
    a, b = 1, 1
    lit = [None] * n
    for i in range(n):
        lit[i] = b
        a, b = b, a + b
    return lit


def main_func_fb(n):
    for i in func_fb(n):
        print(i, end='  ')


# main_fb(29999)
# main_func_fb(21)


# -----------------------------------------------------------
# 
# -----------------------------------------------------------

def func_abc():
    pass

# func_abc()
