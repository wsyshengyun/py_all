
# 关于类

两种关系:
关系一: 类成员与实例成员的关系
关系二:父类与子类的关系
实例是可以访问类的成员的,但类的成员不能访问实例成员  
子类继承父类的类成员和实例成员

对属性的访问遵循的一个优先级:
1, 实例属性
2, 类属性
3, 父类的属性
4, __getattr__() 访问一个不存在的属性时候发生的行为

python 中的 "对象的控制方法  
 __getattribute__ 方法
 当属性被访问的时候发生的行为  
 称为属性拦截器
 重新定义它,要小心无限递归的发生  
 当属性被调用时引起此方法的调用;  属性也包括实例方法  
 ]]参数是什么?

```python
def __getattribute__(self, key):
    return super(Dog, self).__getattribute__(key)
```

如果改为 return self.fun()  
则会引起无限递归
也就是此方法里面不能出现self.***

## 闭包

在一个外函数中定义了一个内函数,内函数里运用了外函数的临时变量，并且外函数返回值是内函数的引用。这样就构成了闭包；

- 这个临时变量可以在外函数内且在内函数外定义，也可以是out_func的参数
- 外函数返回内函数的名字

> 一般情况下，外函数结束后，函数内所有东西都要释放掉，局部变量都会消失，但是闭包是一种特殊的情况，如果外函数的临时变量在内函数里有用到，就不会被释放。




### 闭包中修改外函数的临时变量

python3中可以用nonlocal关键字声明一个变量，表示这个变量不是局部变量空间的变量，需要向上一层变量空间找这个变量。
> nonlocal是在内函数内使用的

python2中，没有这个nonlocal关键字，我们可以把闭包变量改成可变类型的数据进行修改。

开启内函数就是inner_func = out_func()，开启内函数后每次使用inner_func(*args)都是同一份闭包变量。

### 闭包实例

闭包实例：  inner_func = out_func(*args)中inner_func称为闭包实例。

- 闭包中的引用的自由变量（外部函数的局部变量）只和具体的闭包有关联，闭包的每个实例引用的自由变量互不干扰。
- 一个闭包实例对其自由变量的修改，会被传递到下一次该实例的调用。

### 闭包其它

闭包无法修改外部函数的局部变量，除非这个变量一个上可变的对象，比如列表之类的。
闭包可以在一个循环里面。
返回闭包中不要引用任何一个循环变量，或者后后续会变化的的变量

## 装饰器

第二层函数可以用一个_开始_,第三层函数可以用二个_开始 __

### 带参数的装饰器

首层函数的参数为装饰器的参数，
第二层函数的参数为被装饰的函数名字，
第三层函数的参数为被装饰的函数的参数.
