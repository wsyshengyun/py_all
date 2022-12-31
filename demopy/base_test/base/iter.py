'''


可迭代是任何你可以用 Python 中的 for 循环遍历的东西。
可迭代意味着可以遍历，任何可以遍历(for循环)的东西都是可迭代的。
序列只是一种可迭代的类型，但是 Python 也有许多其他种类的迭代器。

集合不是序列，所以它们不支持索引。

名词
    可迭代的
    迭代器
    迭代器协议
    星型表达式
    多重赋值
    生成器是迭代器

'''

'''
    迭代器
可以传递给 next 函数，它将给出下一项，如果没有下一项，那么它将会引发 StopIteration 异常
可以传递给 iter 函数，它会返回一个自身的迭代器
这些语句反过来也是正确的：

    Python 中的迭代器协议。
任何可以在不引发 TypeError 异常的情况下传递给 iter 的东西都是可迭代的
任何可以在不引发 TypeError 异常的情况下传递给 next 的东西都是一个迭代器
当传递给 iter 时，任何返回自身的东西都是一个迭代器

    Python 的许多内置类型也是迭代器。
例如，Python 的 enumerate 和 reversed 对象就是迭代器
在 Python 3 中，zip, map 和 filter 也是迭代器。
Python 中的文件对象也是迭代器。
>>> next(open('hello.txt'))


sum函数与迭代器: sum函数可以接受一个迭代器
对迭代器使用list或者tuple()函数, 也就是对其进行完全的迭代,完全的释放
当我们在迭代器上调用iter时,它返回的也是迭代器,具体说返回的是它自己
迭代器是没有长度的,所以它不能被索引, 也不能求len

对迭代器可以
1 传给next函数
2 使用for循环进行遍历
3 可以传给iter() 它会返回一个自身的迭代器

生成器也是迭代器
多重赋值也适用于迭代器,也可以使用星型表达式
    a, *_, c = aiter
'''

# sum函数与迭代器: sum函数可以接受一个迭代器
L = [1, 2, 3, 4, 5, 6]
aiter = iter(L)
print("sum 一个 迭代器的结果是 {}".format(sum(aiter)))
# len(aiter)  错误

aiter = (i + 1 for i in L)  # 生成器
print("aiter 的类型是: {}".format(type(aiter)))
print("sum -> : {}".format(sum(aiter)))

''' 
 对迭代器使用list或者tuple()函数, 也就是对其进行完全的迭代,完全的释放
 生成器也是迭代器
'''

#
L = [1, 2, 3, 4, 5]

aiter = iter(L)
print(next(aiter))

done_loop = False
while not done_loop:
    try:
        val = next(aiter)
    except StopIteration:
        print("stop!")
        done_loop = True
    else:
        print('val is : {}'.format(val))

L = [1, 2, 4]
aiter = iter(L)
# 多重赋值,也适用于迭代器协议
a, b, c = aiter
print("a = {}, b = {}, c = {}".format(a, b, c))
# 星型表达式,也适用于迭代器
aiter = iter(L)
# 注意这里, 列表又增加了元素
L.append(5)
L.append(6)
# 注意,星型表达式
a, *b, c = aiter
print("a is {}, b is {}, c is {}".format(a, b, c))

# 生成器也是迭代器
L = [1, 2, 3, 4]
G = (i ** 2 for i in L)
print("G  type is {}".format(type(G)))

# 生成器是迭代器,就可以使用next函数了
print(next(G))  # 1
print(next(G))  # 4
print(next(G))  # 9

# 当我们在迭代器上调用iter时,它返回的也是迭代器,具体说返回的是它自己
g1 = iter(G)
print(g1 is G)  # True

''' 当我们进行第二次遍历的时候,将一无所获'''
''' 你可以把迭代器看做是惰性迭代器,它们是一次性使用, 这意味着它们只能遍历一次'''
aiter = iter(L)
l1 = list(aiter)
l2 = list(aiter)
print("l1 is {}".format(l1))  # [1,2,3,4]
print("l2 is {}".format(l2))  # []

'''
 从Set释放可以创建迭代器
'''
_set = {1, 3, 4, 5, 5}
print('_set is {}'.format(_set))
aiter = iter(_set)
print('由set创建的iter: {}'.format(aiter))
print("下一项是: {}".format(next(aiter)))
print("下一项是: {}".format(next(aiter)))

'''
在自定义类中使用迭代器
'''


class Reverse(object):
    """
    相反,逆转
    """

    def __init__(self, data):
        self.data = data
        self.index = len(self.data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        else:
            self.index -= 1
            return self.data[self.index]


reverse_obj = Reverse([1, 2, 3, 4, 5])
for i in reverse_obj:
    print("i is {}".format(i))

'''
创建一个迭代器类
'''


class MyIterator(object):

    def __init__(self):
        self.list = []
        self.posititon = 0
        pass

    def add_name(self, name):
        self.list.append(name)

    def __iter__(self):
        return self

    def __next__(self):
        if self.posititon < len(self.list):
            item = self.list[self.posititon]
            self.posititon += 1
            return item
        else:
            raise StopIteration


obj_my_iterator = MyIterator()
obj_my_iterator.add_name('wsy')
obj_my_iterator.add_name('lrf')
obj_my_iterator.add_name('ll')
obj_my_iterator.add_name('ch')
obj_my_iterator.add_name('yg')
print("MyIterator类中列表为:{}".format(obj_my_iterator.list))  # ['wsy', 'lrf'...]
for i in obj_my_iterator:
    print("MyIterator 类的元素挨个迭代: {}".format(i))
#         wsy
#         lrf
#         ll
#         ch
#         yg

# 判断一个对象是否是一个迭代器
import collections

print("[] 是否是一个可迭代对象: {}".format(isinstance([], collections.Iterable)))
