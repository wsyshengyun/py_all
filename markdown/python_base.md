## 



### 语句与表达式





### 列表推导式

```
def get_headers(header_raw):  
			return dict(line.split(": ", 1) for line in header_raw.split("\n"))  
```



### 字典

#### 字典添加字典

```
dic = {1:2} 
newdic = {'a':1}.update(dic)   # 这种写是错误的  结果为None  
----------------
newdic = {'a':1}
newdic.update(dic)


```

### json

dataStr = json.dumps(python对象)  :   编码成json格式的字符串(机器可以识别的)

datapython = json.loads(strpython) : 解码成python对象(解码为人可以识别的)

与文件打交道

json.dump(python对象, file):   将json写入文件 ; 返回None

datapython = json.load(file): 读取json文件 

> json需要一次性写入,不能以追加的方式多次写入, 否则读取的时候就会出错;





### 文件

文件中间插入字符串

需要把文件读取出来,修改后再全部写入文件.  



### 技巧

#### lambda 作为判断条件



### 类

### super(类名,self)

super() 函数是用于调用父类(超类)的一个方法。

super 是用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没问题，但是如果使用多继承，会涉及到查找顺序（MRO）、重复调用（钻石继承）等种种问题。



> 当obja.\_\_class\_\_ = objb.\_\_class\_\_ 时, obja的成员并不会改变,但是obja的方法变成objb的方法了.

### 库

生成测试用的库

pip install faker   而不是pip install faker-factory   

​	

python运行文件的方式

两种

一种是python xx.py;另外一种是python -m xx

第一种是文件当前的路径加入sys.path，第二种是把输入命令的目录（也就是当前路径）放入了sys.path的属性中。



>  直接运行：要运行的文件不能使用相对导入 ； 



#### 自定义的模块放在哪里？

使用PYTHONPATH环境变量，在这个环境变量里输入相关的路径；不同的路径之间用逗号分开；如果不存在可以创建此环境变量；



#### python库中的省略号的意思

总结一下：
1.省略号在python里也是个对象。
2.=...（赋值号后面省略号），给该变量赋值一个default值。具体python的机制我不清楚。应该是在类里面定义好的。
3.: ...(冒号后面省略号)，表示函数的定义内容不写了。



python

装饰器
	发生在定义函数的时候
	表示方法：
		在def上面加上@装饰器名称
	装饰器本身
		返回一个函数
	装饰器参数
		被包装的函数的名字和其参数 
		func, *args, **kwargs
		
我的理解 
	一般函数关注的就是输入--参数， 输出--return  ，函数的名称， 函数的功能描述  
	关于装饰器
		最外层的函数的参数一定是被装饰的函数的名称  
		内层的函数的参数是被装饰的函数的参数 *args， **kwargs  
		

		最外层的函数返回是内层的包装函数的名称  
		内层函数返回的是被装饰的函数的执行结果  



### 函数

#### 魔法函数：

​	___setattr__（self, name, value)
​		当运行self.name = value 时调用此函数  
​		其参数为 name, value 
​		

	__getattr__(self, name) 当属性name不存时会被调用 
		AttributeError: 'super' object has no attribute '__getattr__'
	__getattribute__(self,name)  无论何时都会被调用 
	__delattr__(self, name) 
		当运行del obj.name(属性名称)时被调用 
		
	删除一个属性时 del obj.name 
		先调用了__delattr__ 然后又调用了__del__ 
		删除一个对象obj时，只调用了__del__

----------------------------------------------
#### 迭代器

​	__iter__如果一个类实现了此方法，那么这个类是可可迭代的
​	

	实现了__next__（）方法的对象就是一个迭代器
	
	让一个迭代器工作至少要实现__iter__和next()方法
	
	for...in...  直到遇到Stopiteration错误时退出循环。
	我们首先要知道什么是可迭代的对象（可以用for循环的对象）Iterable：

理解
	可迭代的  iterable  迭代器 iterator
	可迭代 升级为 迭代器  要实现next方法  
	

##### python中可迭代的对象

​	一类：list，tuple，dict，set，str
​	二类：generator，包含生成器和带yield的generatoe function
​	而生成器不但可以作用于for，还可以被next()函数不断调用并返回下一个值，可以被next()函数不断返回下一个值的对象称为迭代器：Iterator
​	生成器都是Iterator对象，但list，dict，str是Iterable，但不是Iterator，要把list，dict，str等Iterable转换为Iterator可以使用iter()函数

	next()用法：
	next(iterator[, default])
	iterator -- 可迭代对象
	default -- 可选，用于设置在没有下一个元素时返回该默认值，如果不设置，又没有下一个元素则会触发 StopIteration 异常。


​	
iter() 函数的理解
​	参数可以是一个列表

迭代的理解
	对计算机特定程序中需要反复执行的子程序*(一组指令)，进行一次重复，即重复执行程序中的循环，直到满足某条件为止，亦称为迭代。

	迭代是重复反馈过程的活动，其目的通常是为了逼近所需目标或结果。每一次对过程的重复称为一次“迭代”，而每一次迭代得到的结果会作为下一次迭代的初始值。重复执行一系列运算步骤，从前面的量依次求出后面的量的过程。
	
	重复，反馈 过程
	迭代有结果，下一次的初始值
	
	1 有一个初始值  2 变量如何更新 3 终止条件


​	
​	迭代就是改变或者说变化的意思可能是新增一个功能也可能是将一个繁琐的交互简化为一个简单的交互，也可能是将其中一些无效的功能去除，只要和原先的版本功能不同皆可称为迭代

迭代和递归的区别
	迭代是环形结构，递归是树型结构
	迭代可以转递归，但是反过来不行
	
##### 一些类库

​	collection.abs里面的Iterator和Iterable配合isinstance



### 文件的读写

sentinel
/ˈsent(ə)nəl/
名词: 哨兵, 岗哨, 步哨, 岗



使用 x模式，就可以有效防止文件被不小心覆盖的问题。如果要写二进制文件，那么可以把 x改写为 xb。不过需要注意，这种写法只有Python 3才能使用。Python 2是不能这样写的。

'r'：读
'w'：写
'a'：追加
'r+' == r+w（可读可写，文件若不存在就报错(IOError)）
'w+' == w+r（可读可写，文件若不存在就创建）
'a+' ==a+r（可追加可写，文件若不存在就创建）
对应的，如果是二进制文件，就都加一个b就好啦：
'rb'　　'wb'　　'ab'　　'rb+'　　'wb+'　　'ab+'

### python字符串

'r'是防止字符转义的 如果路径中出现'\t'的话 不加r的话\t就会被转义 而加了'r'之后'\t'就能保留原有的样子
在字符串赋值的时候 前面加'r'可以防止字符串在时候的时候不被转义 原理是在转义字符前加'\'

#### 文件路径

1,  引号 + 双反斜杠  'c:\\_python'
2,  r + 引号 + 单反斜杠   r'c:\_python''