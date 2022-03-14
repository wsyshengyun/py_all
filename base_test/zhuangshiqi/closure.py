# coding:utf8
""" closure
    闭包
 """
def print_msg():
    msg = "Tm closure" 
    def printer():
        print(msg)
    return printer 

closure = print_msg() 
closure() 

def startAt(x):
    def incrementBy(y):
        return x+y
    return incrementBy

d = startAt(1)
print(d(2))
print(d(3))


# -----------------------------------------------------------
# 
# -----------------------------------------------------------

# 
print("#"*30)
list2 = []
for j in range(4):
    def func(c):
        return c*j
    list2.append(func)

for f in list2:
    print(f(2))



print("#"*30)
lit = []
for i in range(4):
    def fp(i): # 这里的i不等于上面的i；这是一个形参
        def _inner(x):
            return x*i
        return _inner
    lit.append(fp(i))
# 
for f in lit:
    print(f(2))

# -----------------------------------------------------------
# 闭包的实例 关于坐标点的移动
# -----------------------------------------------------------
print("闭包的实例应用，关于坐标的移动")
origin = [0,0]
def create(pos=origin):
    def go(direction, step):
        new_x = pos[0] + direction[0] * step 
        new_y = pos[1] + direction[1] * step 
        pos[0], pos[1] = new_x, new_y
        return pos
    return go

player = create()
print(player([1,0], 10))
print(player([0,1], 20))
print(player([-1,0], 10))