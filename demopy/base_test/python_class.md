## super  

​	super（子类自身的名字，self） ==> 这等于是 父类 
​	然后可以调用父类的方法
​	super(子类自身的名字，self).父类的方法名字（）
​	

	1. super并不是一个函数，是一个类名，形如super(B, self)事实上调用了super类的初始化函数，
	   产生了一个super对象；
　　2. super类的初始化函数并没有做什么特殊的操作，只是简单记录了类类型和具体实例；
　　3. super(B, self).func的调用并不是用于调用当前类的父类的func函数；
　　4. Python的多继承类是通过mro的方式来保证各个父类的函数被逐一调用，而且保证每个父类函数
       只调用一次（如果每个类都使用super）；
　　5. 混用super类和非绑定的函数是一个危险行为，这可能导致应该调用的父类函数没有调用或者一
       个父类函数被调用多次。



## python属性的访问

我们在类的内部定义了\_\_getattribute\_\_方法，就会打破原有属性查找方式，在obj.value查找属性时，Python会无条件调用\_\_getattribute\_\_方法。

 

值得注意的是，一般我们很少会重写定义\_\_getattribute\_\_方法，因为类的属性获取方式相当重要，而我们一旦写不好\_\_getattribute\_\_方法，属性获取就会变得非常混乱。

### 内置方法\_\_get\_\_

\_\_get\_\_内置方法与上面两个方法不同，它的作用是为了把一个类的实例当做描述符来用，与它一起作用的还有\_\_set\_\_、\_\_delete\_\_方法。

\_\_get\_\_、\_\_set\_\_、\_\_delete\_\_

l 类定义任何上面三个方法的任意一个，类的实例就会被认为是一个描述符

l 类同时定义了\_\_get\_\_和 \_\_set\_\_方法，它的实例被认为是一个数据描述符

l 只定义 \_\_get\_\_方法被认为是非数据描述符

l 数据和非数据描述符的区别：如果一个实例的字典有和数据描述符同名的属性，那么数据描述符会被优先使用；实例的字典实现了非数据描述符的定义，那么这个字典中的属性会被优先使用

l 只读数据描述符：类中同时定义\_\_get\_\_和\_\_set\_\_方法，且在\_\_set\_\_方法中抛出AttributeError异常

### 内置方法\_\_getattr\_\_

如果你在obj的类里定义了\_\_getattr\_\_方法，当我们使用正常的属性访问都找不到属性时，会调用这个\_\_getattr\_\_方法

 

正常情况下,如果类中重新定义了\_\_getattribute\_\_,那么就不会再调用\_\_getattr\_\_ 

不管能不能找到属性

 

### Python中对象属性的获取链

我们在使用obj.value时，Python内部是怎么样的查找顺序呢？（value不是数据描述符，数据描述符请看下面）

obj.value等价于getattr(obj, 'value')，会调用基类object Python默认的\_\_getattribute\_\_方法，该方法逻辑如下

最开始，Python会使用obj.\_\_dict\_\_[vlaue]的方法查找，也就是查找对象内置字典的key值

如果上述方法查找不到，会使用type(obj).\_\_dict\_\_[value]来查找，也就是会查找obj的类的属性

如果上述方法查找不到，Python会用mro的查找方法遍历type(obj)的基类，在其基类中查找类属性，直到找到为止

如果还找不到，\_\_getattribute\_\_在抛出AttributeError前调用\_\_getattr\_\_方法

 

#### 属性的获取2

当类中定义了\_\_slots\_\_属性时，对象就不会有\_\_dict\_\_属性了，这时访问属性时，是通过类似描述符的方式查找属性的。
    一般情况下，python的属性访问机制是：实例属性，类属性，父类属性，object属性；也就是先查找实例对象的\_\_dict\_\_属性，没有的话再查找类\_\_dict\_\_属性，再没有的话查找父类的\_\_dict\_\_属性，最后是基类object属性。当定义了数据描述符时时，会覆盖实例对象的\_\_dict\_\_属性；非数据描述符访问属性时，先查找对象的\_\_dict\_\_属性，没有的话再调用描述符的\_\_get\_\_方法。





 

 

在Python中，访问一个属性的优先级顺序按照如下顺序:
1、\_getattribute\_()
2.类属性
3.数据描述符
4.实例属性
5.非数据描述符
6.\_\_getattr\_\_()方法

### 描述符对象

#### 描述符有什么用和好处

1）一般情况下不会用到，建议：先定基本的，以后真有需要再扩展。别贪玩。
2）可以在设置属性时，做些检测等方面的处理
3）缓存？
4）设置属性不能被删除？那定义\_delete\_方法，并raise 异常。
5）还可以设置只读属性
6）把一个描述符作为某个对象的属性。这个属性要更改，比如增加判断，或变得更复杂的时候，所有的处理只要在描述符中操作就行了。

 

 

 

#### 如何检测一个对象是不是描述符？

如果把问题换成——一个对象要满足什么条件，它才是描述符呢——那是不是回答就非常简单了？
答：只要定义了（set,get,delete）方法中的任意一种或几种，它就是个描述符。
那么，继续问：怎么判断一个对象定义了这三种方法呢？
立马有人可能就会回答：你是不是傻啊？看一下不就看出来了。。。
问题是，你看不到的时候呢？python内置的staticmethod，classmethod怎么看？
正确的回答应该是：看这个对象的\_dict\_。
要看对象的\_dict\_好办，直接dir(对象）就行了。现在可以写出检测对象是不是描述符的方法了：

def has\_descriptor\_attrs(obj):

  return set(['\_\_get\_\_', '\_\_set\_\_', '\_\_delete\_\_']).intersection(dir(obj))

 

def is\_descriptor(obj):

  """obj can be instance of descriptor or the descriptor class"""

  return bool(has\_descriptor\_attrs(obj))

 

def has\_data\_descriptor\_attrs(obj):

  return set(['\_\_set\_\_', '\_\_delete\_\_']) & set(dir(obj))

 

def is\_data\_descriptor(obj):

  return bool(has\_data\_descriptor\_attrs(obj))

 

测试一下：

 

print is\_descriptor(classmethod), is\_data\_descriptor(classmethod)

print is\_descriptor(staticmethod), is\_data\_descriptor(staticmethod)

print  is\_data\_descriptor(property)

 

输出： 

(True, False) 

(True, False) 

True 

看来，特性（property）是数据描述符

 

 

### \_\_dict\_\_

 自定义属性都会有一个字典\_\_dict\_\_，包含了所有的实例属性，不包含实例方法

  实例的\_\_dict\_\_包含了实例属性y，但是不会有实例方法func和类属性x。类的\_\_dict\_\_包含了其余的东西（类属性，实例方法，静态方法，类方法等）。

类的Dict   ==>  TestDesc: __dict__: 

{

'\_\_module\_\_': '\_\_main\_\_',

 'x': <\_\_main\_\_.Desc object at 0x00000000026F82E8>,

 '\_\_init\_\_': <function TestDesc.\_\_init\_\_ at 0x00000000026E4488>, 

'\_\_getattribute\_\_': <function TestDesc.\_\_getattribute\_\_ at 0x00000000026E4510>,

'\_\_dict\_\_': <attribute '\_\_dict\_\_' of 'TestDesc' objects>, 

'\_\_weakref\_\_': <attribute '\_\_weakref\_\_' of 'TestDesc' objects>,

 '\_\_doc\_\_': None

}

 

### 如何重写\_\_getattribute\_\_

同时覆盖掉getattribute和getattr的时候，在getattribute中需要模仿原本的行为抛出AttributeError或者手动调用getattr

class AboutAttr(object):

  def \_\_init\_\_(self, name):

​    self.name = name

 

  def \_\_getattribute\_\_(self, item):

​    try:

​      return super(AboutAttr, self).\_\_getattribute\_\_(item)

​    except KeyError:

​      return 'default'

​    except AttributeError as ex:

​      print ex



### 运算符重载

| \_\_new\_\_                                                  | 创建类，在 \_\_init\_\_ 之前创建对象                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| \_\_init\_\_                                                 | 类的构造函数，其功能是创建类对象时做初始化工作。             |
| \_\_del\_\_                                                  | 析构函数，其功能是销毁对象时进行回收资源的操作               |
| \_\_add\_\_                                                  | 加法运算符 +，当类对象 X 做例如 X+Y 或者 X+=Y 等操作，内部会调用此方法。但如果类中对 \_\_iadd\_\_ 方法进行了重载，则类对象 X 在做 X+=Y 类似操作时，会优先选择调用 \_\_iadd\_\_ 方法。 |
| \_\_radd\_\_                                                 | 当类对象 X 做类似 Y+X 的运算时，会调用此方法。               |
| \_\_iadd\_\_                                                 | 重载 += 运算符，也就是说，当类对象 X 做类似 X+=Y 的操作时，会调用此方法。 |
| \_\_or\_\_                                                   | “或”运算符 \|，如果没有重载 \_\_ior\_\_，则在类似 X\|Y、X\|=Y 这样的语句中，“或”符号生效 |
| \_\_repr\_\_，\_\_str\_\_                                    | 格式转换方法，分别对应函数 repr(X)、str(X)                   |
| \_\_call\_\_                                                 | 函数调用，类似于 X(*args, **kwargs) 语句                     |
| \_\_getattr\_\_                                              | 点号运算，用来获取类属性                                     |
| \_\_setattr\_\_                                              | 属性赋值语句，类似于 X.any=value                             |
| \_\_delattr\_\_                                              | 删除属性，类似于 del X.any                                   |
| \_\_getattribute\_\_                                         | 获取属性，类似于 X.any                                       |
| \_\_getitem\_\_                                              | 索引运算，类似于 X[key]，X[i:j]                              |
| \_\_setitem\_\_                                              | 索引赋值语句，类似于 X[key], X[i:j]=sequence                 |
| \_\_delitem\_\_                                              | 索引和分片删除                                               |
| \_\_get\_\_, \_\_set\_\_, \_\_delete\_\_                     | 描述符属性，类似于 X.attr，X.attr=value，del X.attr          |
| \_\_len\_\_                                                  | 计算长度，类似于 len(X)                                      |
| \_\_lt\_\_，\_\_gt\_\_，\_\_le\_\_，\_\_ge\_\_，\_\_eq\_\_，\_\_ne\_\_ | 比较，分别对应于 <、>、<=、>=、=、!= 运算符。                |
| \_\_iter\_\_，\_\_next\_\_                                   | 迭代环境下，生成迭代器与取下一条，类似于 I=iter(X) 和 next() |
| \_\_contains\_\_                                             | 成员关系测试，类似于 item in X                               |
| \\_\_index\_\_                                               | 整数值，类似于 hex(X)，bin(X)，oct(X)                        |
| \_\_enter\_\_，\_\_exit\_\_                                  | 在对类对象执行类似 with obj as var 的操作之前，会先调用 \_\_enter\_\_ 方法，其结果会传给 var；在最终结束该操作之前，会调用 \_\_exit\_\_ 方法（常用于做一些清理、扫尾的工作） |

```
class MyClass: #自定义一个类
    def __init__(self, name , age): #定义该类的初始化函数
        self.name = name #将传入的参数值赋值给成员交量
        self.age = age
    def __str__(self): #用于将值转化为字符串形式，等同于 str(obj)
        return "name:"+self.name+";age:"+str(self.age)
   
    __repr__ = __str__ #转化为供解释器读取的形式
   
    def __lt__(self, record): #重载 self<record 运算符
        if self.age < record.age:
            return True
        else:
            return False
   
    def __add__(self, record): #重载 + 号运算符
        return MyClass(self.name, self.age+record.age)

myc = MyClass("Anna", 42) #实例化一个对象 Anna，并为其初始化
mycl = MyClass("Gary", 23) #实例化一个对象 Gary，并为其初始化
print(repr(myc)) #格式化对象 myc，
print(myc) #解释器读取对象 myc，调用 repr
print (str (myc)) #格式化对象 myc ，输出"name:Anna;age:42"
print(myc < mycl) #比较 myc<mycl 的结果，输出 False
print (myc+mycl) #进行两个 MyClass 对象的相加运算，输出 "name:Anna;age:65"
```



### 魔法方法

有的魔法方法有返回值的，比如\\__\_str\_\_() \\_\_len\_\_()，有的是没有返回值的，比如\_\_init\_\_()

 

####  \_\_new\_\_

 \_\_new\_\_ 决定是否要使用该 \_\_init\_\_ 方法，因为\_\_new\_\_ 可以调用其他类的构造方法或者直接返回别的实例对象来作为本类的实例，如果 \_\_new\_\_ 没有返回实例对象，则\_\_init\_\_ 不会被调用。

\_\_new\_\_() 是一种负责创建类实例的静态方法，它无需使用 staticmethod 装饰器修饰，且该方法会优先 \_\_init\_\_() 初始化方法被调用。
么，什么情况下使用 \_\_new\_\_() 呢？答案很简单，在 \_\_init\_\_() 不够用的时候。

例如，前面例子中对 Python 不可变的内置类型（如 int、str、float 等）进行了子类化，这是因为一旦创建了这样不可变的对象实例，就无法在 \_\_init\_\_() 方法中对其进行修改。

有些读者可能会认为，\_\_new\_\_() 对执行重要的对象初始化很有用，如果用户忘记使用 super()，可能会漏掉这一初始化。虽然这听上去很合理，但有一个主要的缺点，即如果使用这样的方法，那么即便初始化过程已经是预期的行为，程序员明确跳过初始化步骤也会变得更加困难。不仅如此，它还破坏了“\_\_init\_\_() 中执行所有初始化工作”的潜规则。


一般情况下，覆写 \_\_new\_\_() 的实现将会使用合适的参数调用其超类的 super().\_\_new\_\_()，并在返回之前修改实例。

 

 

#### \_\_del\_\_(self)

   有了构造函数自然少不了析构函数。Python中\_\_del\_\_可以认为是析构函数了，在一个实例被销毁时它会执行。该方法是解释器自动调用的，一般情况下不重写。

 

大多数情况下，Python 开发者不需要手动进行垃圾回收，因为 Python 有自动的垃圾回收机制（下面会讲），能自动将不需要使用的实例对象进行销毁。

无论是手动销毁，还是 Python 自动帮我们销毁，都会调用 \_\_del\_\_() 方法。举个例子：

class CLanguage:

  def \_\_init\_\_(self):

​    print("调用 \_\_init\_\_() 方法构造对象")

  def \_\_del\_\_(self):

​    print("调用\_\_del\_\_() 销毁对象，释放其空间")

clangs = CLanguage()

del clangs

程序运行结果为：

调用 \_\_init\_\_() 方法构造对象
调用\_\_del\_\_() 销毁对象，释放其空间


但是，读者千万不要误认为，只要为该实例对象调用 \_\_del\_\_() 方法，该对象所占用的内存空间就会被释放。举个例子：

class CLanguage:

  def \_\_init\_\_(self):

​    print("调用 \_\_init\_\_() 方法构造对象")

  def \_\_del\_\_(self):

​    print("调用\_\_del\_\_() 销毁对象，释放其空间")

clangs = CLanguage()

\#添加一个引用clangs对象的实例对象

cl = clangs

del clangs

print("***********")

程序运行结果为：

调用 \_\_init\_\_() 方法构造对象
***********
调用\_\_del\_\_() 销毁对象，释放其空间

注意，最后一行输出信息，是程序执行即将结束时调用 \_\_del\_\_() 方法输出的。

可以看到，当程序中有其它变量（比如这里的 cl）引用该实例对象时，即便手动调用 \_\_del\_\_() 方法，该方法也不会立即执行。这和 Python 的垃圾回收机制的实现有关。

Python 采用自动引用计数（简称 ARC）的方式实现垃圾回收机制。该方法的核心思想是：每个 Python 对象都会配置一个计数器，初始 Python 实例对象的计数器值都为 0，如果有变量引用该实例对象，其计数器的值会加 1，依次类推；反之，每当一个变量取消对该实例对象的引用，计数器会减 1。如果一个 Python 对象的的计数器值为 0，则表明没有变量引用该 Python 对象，即证明程序不再需要它，此时 Python 就会自动调用 \_\_del\_\_() 方法将其回收。

以上面程序中的 clangs 为例，实际上构建 clangs 实例对象的过程分为 2 步，先使用 CLanguage() 调用该类中的 \_\_init\_\_() 方法构造出一个该类的对象（将其称为 C，计数器为 0），并立即用 clangs 这个变量作为所建实例对象的引用（ C 的计数器值 + 1）。在此基础上，又有一个 clang 变量引用 clangs（其实相当于引用 CLanguage()，此时 C 的计数器再 +1 ），这时如果调用del clangs语句，只会导致 C 的计数器减 1（值变为 1），因为 C 的计数器值不为 0，因此 C 不会被销毁（不会执行 \_\_del\_\_() 方法）。

如果在上面程序结尾，添加如下语句：

del cl

print("-----------")

则程序的执行结果为：

调用 \_\_init\_\_() 方法构造对象
***********
调用\_\_del\_\_() 销毁对象，释放其空间
\-----------

可以看到，当执行 del cl 语句时，其应用的对象实例对象 C 的计数器继续 -1（变为 0），对于计数器为 0 的实例对象，Python 会自动将其视为垃圾进行回收。

需要额外说明的是，如果我们重写子类的 \_\_del\_\_() 方法（父类为非 object 的类），则必须显式调用父类的 \_\_del\_\_() 方法，这样才能保证在回收子类对象时，其占用的资源（可能包含继承自父类的部分资源）能被彻底释放。为了说明这一点，这里举一个反例：

[纯文本](http://c.biancheng.net/view/2371.html)[复制](http://c.biancheng.net/view/2371.html)

class CLanguage:

  def \_\_del\_\_(self):

​    print("调用父类 \_\_del\_\_() 方法")

 

class cl(CLanguage):

  def \_\_del\_\_(self):

​    print("调用子类 \_\_del\_\_() 方法")

c = cl()

del c

程序运行结果为：

调用子类 \_\_del\_\_() 方法

 

 

#### \_\_str\_\_(self)  ??

#### \_\_repr\_\_(self)

前面章节中，我们经常会直接输出类的实例化对象，例如：

class CLanguage:

  pass

clangs = CLanguage()

print(clangs)

程序运行结果为：

<\_\_main\_\_.CLanguage object at 0x000001A7275221D0>

通常情况下，直接输出某个实例化对象，本意往往是想了解该对象的基本信息，例如该对象有哪些属性，它们的值各是多少等等。但默认情况下，我们得到的信息只会是“类名+object at+内存地址”，对我们了解该实例化对象帮助不大。

那么，有没有可能自定义输出实例化对象时的信息呢？答案是肯定，通过重写类的 \_\_repr\_\_() 方法即可。事实上，当我们输出某个实例化对象时，其调用的就是该对象的 \_\_repr\_\_() 方法，输出的是该方法的返回值。

以本节开头的程序为例，执行 print(clangs) 等同于执行 print(clangs.\_\_repr\_\_())，程序的输出结果是一样的（输出的内存地址可能不同）。

和 \_\_init\_\_(self) 的性质一样，[Python](http://c.biancheng.net/python/) 中的每个类都包含 \_\_repr\_\_() 方法，因为 object 类包含 \_\_reper\_\_() 方法，而 Python 中所有的类都直接或间接继承自 object 类。

默认情况下，\_\_repr\_\_() 会返回和调用者有关的 “类名+object at+内存地址”信息。当然，我们还可以通过在类中重写这个方法，从而实现当输出实例化对象时，输出我们想要的信息。

举个例子：

class CLanguage:

  def \_\_init\_\_(self):

​    self.name = "C语言中文网"

​    self.add = "http://c.biancheng.net"

  def \_\_repr\_\_(self):

​    return "CLanguage[name="+ self.name +",add=" + self.add +"]"

clangs = CLanguage()

print(clangs)

程序运行结果为：

CLanguage[name=C语言中文网,add=http://c.biancheng.net]

由此可见，\_\_repr\_\_() 方法是类的实例化对象用来做“自我介绍”的方法，默认情况下，它会返回当前对象的“类名+object at+内存地址”，而如果对该方法进行重写，可以为其制作自定义的自我描述信息

函数str() 用于将值转化为适于人阅读的形式，而repr() 转化为供解释器读取的形式，某对象没有适于人阅读的解释形式的话，str() 会返回与repr()，所以print展示的都是str的格式。例子：

 

#### \_\_getattr\_\_(self[,…])

   当我们访问一个不存在的属性时会调用此方法，如果属性存在则不会调用。

#### \_\_setattr\_\_(self, name, value)

   所有的属性设置都会调用此方法，并且只有拥有这个魔法方法的对象才可以设置属性。使用这个方法要注意不要循环调用了。

 

#### \_\_getattribute\_\_(self, item)

   给方法和\_\_getattr\_\_方法类似，但是它更加强大，所有访问属性的行为都会调用这个方法，不仅仅是不存在的属性。

 

 

 

#### \_\_call\_\_() 

 

本节再介绍 [Python](http://c.biancheng.net/python/) 类中一个非常特殊的实例方法，即 \_\_call\_\_()。该方法的功能类似于在类中重载 () 运算符，使得类实例对象可以像调用普通函数那样，以“对象名()”的形式使用。

举个例子：

class CLanguage:

  \# 定义\_\_call\_\_方法

  def \_\_call\_\_(self,name,add):

​    print("调用\_\_call\_\_()方法",name,add)

 

clangs = CLanguage()

clangs("C语言中文网","http://c.biancheng.net")

程序执行结果为：

调用\_\_call\_\_()方法 C语言中文网 http://c.biancheng.net

可以看到，通过在 CLanguage 类中实现 \_\_call\_\_() 方法，使的 clangs 实例对象变为了可调用对象。

Python 中，凡是可以将 () 直接应用到自身并执行，都称为可调用对象。可调用对象包括自定义的函数、Python 内置函数以及本节所讲的类实例对象。

对于可调用对象，实际上“名称()”可以理解为是“名称.\_\_call\_\_()”的简写。仍以上面程序中定义的 clangs 实例对象为例，其最后一行代码还可以改写为如下形式：

clangs.\_\_call\_\_("C语言中文网","http://c.biancheng.net")

运行程序会发现，其运行结果和之前完全相同。

这里再举一个自定义函数的例子，例如：

def say():

  print("Python教程：http://c.biancheng.net/python")

say()

say.\_\_call\_\_()

程序执行结果为：

Python教程：http://c.biancheng.net/python
Python教程：http://c.biancheng.net/python

不仅如此，类中的实例方法也有以上 2 种调用方式，这里不再举例，有兴趣的读者可自行编写代码尝试。

用 \_\_call\_\_() 弥补 hasattr() 函数的短板

前面章节介绍了 hasattr() 函数的用法，该函数的功能是查找类的实例对象中是否包含指定名称的属性或者方法，但该函数有一个缺陷，即它无法判断该指定的名称，到底是类属性还是类方法。

要解决这个问题，我们可以借助可调用对象的概念。要知道，类实例对象包含的方法，其实也属于可调用对象，但类属性却不是。举个例子：

class CLanguage:

  def \_\_init\_\_ (self):

​    self.name = "C语言中文网"

​    self.add = "http://c.biancheng.net"

  def say(self):

​    print("我正在学Python")

 

clangs = CLanguage()

if hasattr(clangs,"name"):

  print(hasattr(clangs.name,"\_\_call\_\_"))

print("**********")

if hasattr(clangs,"say"):

  print(hasattr(clangs.say,"\_\_call\_\_"))

程序执行结果为：

False
**********
True

可以看到，由于 name 是类属性，它没有以 \_\_call\_\_ 为名的 \_\_call\_\_() 方法；而 say 是类方法，它是可调用对象，因此它有 \_\_call\_\_() 方法。

 

### [Python](http://c.biancheng.net/python/) hasattr()函数

hasattr() 函数用来判断某个类实例对象是否包含指定名称的属性或方法。该函数的语法格式如下：

hasattr(obj, name)

其中 obj 指的是某个类的实例对象，name 表示指定的属性名或方法名。同时，该函数会将判断的结果（True 或者 False）作为返回值反馈回来。

举个例子：

class CLanguage:

  def \_\_init\_\_ (self):

​    self.name = "C语言中文网"

​    self.add = "http://c.biancheng.net"

  def say(self):

​    print("我正在学Python")

 

clangs = CLanguage()

print(hasattr(clangs,"name"))

print(hasattr(clangs,"add"))

print(hasattr(clangs,"say"))

程序输出结果为：
True
True
True

显然，无论是属性名还是方法名，都在 hasattr() 函数的匹配范围内。因此，我们只能通过该函数判断实例对象是否包含该名称的属性或方法，但不能精确判断，该名称代表的是属性还是方法。



### Python getattr() 函数

getattr() 函数获取某个类实例对象中指定属性的值。没错，和 hasattr() 函数不同，该函数只会从类对象包含的所有属性中进行查找。

getattr() 函数的语法格式如下：

getattr(obj, name[, default])

其中，obj 表示指定的类实例对象，name 表示指定的属性名，而 default 是可选参数，用于设定该函数的默认返回值，即当函数查找失败时，如果不指定 default 参数，则程序将直接报 AttributeError 错误，反之该函数将返回 default 指定的值。

举个例子：

class CLanguage:

  def \_\_init\_\_ (self):

​    self.name = "C语言中文网"

​    self.add = "http://c.biancheng.net"

  def say(self):

​    print("我正在学Python")

 

clangs = CLanguage()

print(getattr(clangs,"name"))

print(getattr(clangs,"add"))

print(getattr(clangs,"say"))

print(getattr(clangs,"display",'nodisplay'))

程序执行结果为：

C语言中文网
http://c.biancheng.net
<bound method CLanguage.say of <\_\_main\_\_.CLanguage object at 0x000001FC2F2E3198>>
nodisplay

可以看到，对于类中已有的属性，getattr() 会返回它们的值，而如果该名称为方法名，则返回该方法的状态信息；反之，如果该明白不为类对象所有，要么返回默认的参数，要么程序报 AttributeError 错误。

Python setattr()函数

setattr() 函数的功能相对比较复杂，它最基础的功能是修改类实例对象中的属性值。其次，它还可以实现为实例对象动态添加属性或者方法。

setattr() 函数的语法格式如下：

setattr(obj, name, value)

首先，下面例子演示如何通过该函数修改某个类实例对象的属性值：

class CLanguage:

  def \_\_init\_\_ (self):

​    self.name = "C语言中文网"

​    self.add = "http://c.biancheng.net"

  def say(self):

​    print("我正在学Python")

clangs = CLanguage()

print(clangs.name)

print(clangs.add)

setattr(clangs,"name","Python教程")

setattr(clangs,"add","http://c.biancheng.net/python")

print(clangs.name)

print(clangs.add)

程序运行结果为：

C语言中文网
http://c.biancheng.net
Python教程
http://c.biancheng.net/python


甚至利用 setattr() 函数，还可以将类属性修改为一个类方法，同样也可以将类方法修改成一个类属性。例如：

def say(self):

  print("我正在学Python")

 

class CLanguage:

  def \_\_init\_\_ (self):

​    self.name = "C语言中文网"

​    self.add = "http://c.biancheng.net"

 

clangs = CLanguage()

print(clangs.name)

print(clangs.add)

setattr(clangs,"name",say)

clangs.name(clangs)

程序运行结果为：

C语言中文网
http://c.biancheng.net
我正在学Python

显然，通过修改 name 属性的值为 say（这是一个外部定义的函数），原来的 name 属性就变成了一个 name() 方法。

使用 setattr() 函数对实例对象中执行名称的属性或方法进行修改时，如果该名称查找失败，Python 解释器不会报错，而是会给该实例对象动态添加一个指定名称的属性或方法。例如：

[纯文本](http://c.biancheng.net/view/2378.html)[复制](http://c.biancheng.net/view/2378.html)

def say(self):

  print("我正在学Python")

 

class CLanguage:

  pass

 

clangs = CLanguage()

setattr(clangs,"name","C语言中文网")

setattr(clangs,"say",say)

print(clangs.name)

clangs.say(clangs)

程序执行结果为：

C语言中文网
我正在学Python

可以看到，虽然 CLanguage 为空类，但通过 setattr() 函数，我们为 clangs 对象动态添加了一个 name 属性和一个 say() 方法。

 

 

 

 

## python issubclass和isinstalce

Python](http://c.biancheng.net/python/) 提供了如下两个函数来检查类型：

- issubclass(cls, class\_or\_tuple)：检查 cls 是否为后一个类或元组包含的多个类中任意类的子类。
- isinstance(obj, class\_or\_tuple)：检查 obj 是否为后一个类或元组包含的多个类中任意类的对象。

通过上面程序可以看出，issubclass() 和 isinstance() 两个函数的用法差不多，区别只是 issubclass() 的第一个参数是类名，而 isinstance() 的第一个参数是变量，这也与两个函数的意义对应：issubclass 用于判断是否为子类，而 isinstance() 用于判断是否为该类或子类的实例。

issubclass() 和 isinstance() 两个函数的第二个参数都可使用元组。例如如下代码：

```
data = (20, 'fkit')print('data是否为列表或元组: ', isinstance(data, (list, tuple))) # True# str不是list或者tuple的子类，输出Falseprint('str是否为list或tuple的子类: ', issubclass(str, (list, tuple)))# str是list或tuple或object的子类，输出Trueprint('str是否为list或tuple或object的子类 ', issubclass(str, (list, tuple, object)))
```

ython 为所有类都提供了一个 **`\_\_bases\_\_`** 属性，通过该属性可以查看该类的所有直接父类，该属性返回所有直接父类组成的元组。例如如下代码：

```
class A:    passclass B:    passclass C(A, B):    passprint('类A的所有父类:', A.\_\_bases\_\_)print('类B的所有父类:', B.\_\_bases\_\_)print('类C的所有父类:', C.\_\_bases\_\_)
```

运行上面程序，可以看到如下运行结果：

类A的所有父类: (<class 'object'>,)
类B的所有父类: (<class 'object'>,)
类C的所有父类: (<class '\_\_main\_\_.A'>, <class '\_\_main\_\_.B'>)

从上面的运行结果可以看出，如果在定义类时没有显式指定它的父类，则这些类默认的父类是 object 类。

Python 还为所有类都提供了一个 \_\_subclasses\_\_() 方法，通过该方法可以查看该类的所有直接子类，该方法返回该类的所有子类组成的列表。例如在上面程序中增加如下两行：

```
print('类A的所有子类:', A.\_\_subclasses\_\_())print('类B的所有子类:', B.\_\_subclasses\_\_())
```

运行上面代码，可以看到如下输出结果：

类A的所有子类: [<class '\_\_main\_\_.C'>]
类B的所有子类: [<class '\_\_main\_\_.C'>]





## lambda表达式

lambda 表达式，又称匿名函数，常用来表示内部仅包含 1 行表达式的函数。如果一个函数的函数体仅有 1 行表达式，则该函数就可以用 lambda 表达式来代替。

lambda 表达式的语法格式如下：

name = lambda [list] : 表达式

其中，定义 lambda 表达式，必须使用 lambda 关键字；[list] 作为可选参数，等同于定义函数是指定的参数列表；value 为该表达式的名称。

该语法格式转换成普通函数的形式，如下所示：

```
def name(list):    return 表达式name(list)
```

> 显然，使用普通方法定义此函数，需要 3 行代码，而使用 lambda 表达式仅需 1 行。


举个例子，如果设计一个求 2 个数之和的函数，使用普通函数的方式，定义如下：

```
def add(x, y):    return x+ yprint(add(3,4))
```

程序执行结果为：

7

由于上面程序中，add() 函数内部仅有 1 行表达式，因此该函数可以直接用 lambda 表达式表示：

```
add = lambda x,y:x+yprint(add(3,4))
```

程序输出结果为：

7


可以这样理解 lambda 表达式，其就是简单函数（函数体仅是单行的表达式）的简写版本。相比函数，lamba 表达式具有以下 2 个优势：

- *对于单行函数，使用 lambda 表达式可以省去定义函数的过程，让代码更加简洁；*
- *对于不需要多次复用的函数，使用 lambda 表达式可以在用完之后立即释放，提高程序执行的性能。*

## 迭代器

**`*迭代器指的就是支持迭代的容器*`**

更确切的说，是支持迭代的容器类对象，这里的容器可以是列表、元组等这些 [Python](http://c.biancheng.net/python/) 提供的基础容器，也可以是自定义的容器类对象，只要该容器支持迭代即可。

如果要自定义实现一个迭代器，则类中必须实现如下 2 个方法：

1. \_\_next\_\_(self)：返回容器的下一个元素。
2. \_\_iter\_\_(self)：该方法返回一个迭代器（iterator）。

除此之外，Python 内置的 iter() 函数也会返回一个迭代器，该函数的语法格式如下：

iter(obj[, sentinel])

其中，obj 必须是一个可迭代的容器对象，而 sentinel 作为可选参数，如果使用此参数，要求 obj 必须是一个可调用对象，具体功能后面会讲。

> 可调用对象，指的是该类的实例对象可以像函数那样，直接以“对象名()”的形式被使用。通过在类中添加 __call__() 方法，就可以将该类的实例对象编程可调用对象。有关 __call__() 方法，可阅读《[Python __call__()](http://c.biancheng.net/view/2380.html)》做详细了解。

我们常用的是仅有 1 个参数的 iter() 函数，通过传入一个可迭代的容器对象，我们可以获得一个迭代器，通过调用该迭代器中的 __next__() 方法即可实现迭代。例如；

```
# 将列表转换为迭代器myIter = iter([1, 2, 3])# 依次获取迭代器的下一个元素print(myIter.__next__())print(myIter.__next__())print(myIter.__next__())print(myIter.__next__())
```

运行结果为：

1
2
3
Traceback (most recent call last):
 File "C:\Users\mengma\Desktop\demo.py", line 7, in <module>
  print(myIter.__next__())
StopIteration

> 另外，也可以使用 next() 内置函数来迭代，即 next(myIter)，和 __next__() 方法是完全一样的。

从程序的执行结果可以看出，当迭代完存储的所有元素之后，如果继续迭代，则 __next__() 方法会抛出 StopIteration 异常。

这里介绍 iter() 函数第 2 个参数的作用，如果使用该参数，则要求第一个 obj 参数必须传入可调用对象（可以不支持迭代），这样当使用返回的迭代器调用 __next__() 方法时，它会通过执行 obj() 调用 __call__() 方法，如果该方法的返回值和第 2 个参数值相同，则输出 StopInteration 异常；反之，则输出 __call__() 方法的返回值。

例如，修改 listDemo 类如下所示：

```python
class listDemo:    
	def __init__(self):        
			self.__date=[]        
			self.__step = 0    
	def __setitem__(self,key,value):       
    		self.__date.insert(key,value)        
    		self.__step += 1    #是该类实例对象成为可调用对象    
    def __call__(self):       
    		self.__step-=1        
    		return self.__date[self.__step]
mylist = listDemo()
mylist[0]=1mylist[1]=2
#将 mylist 变为迭代器
a = iter(mylist,1)
print(a.__next__())
print(a.__next__())
```

程序执行结果为：

2
Traceback (most recent call last):
 File "D:\python3.6\1.py", line 20, in <module>
  print(a.\_\_next\_\_())
StopIteration

输出结果中，之所以最终抛出 StopIteration 异常，是因为这里原本要输出的元素 1 和 iter() 函数的第 2 个参数相同。





## 生成器

生成器本质上也是迭代器,不过它比较特殊 

