

### import的作用
方便导入其它Python文件，以使用它的类、方法或者变量，从而达到代码复用的目的。

### sys.path | sys.modules 

sys.path 包含了module的查找路径； 

sys.modules 包含了当前所有load的所有的module的dict（其中包含了builtin的modules）

### 入口文件

例子目录
Tree 
	m1.py
	m2.py
	Branch 
		m3.py

​		m4.py

入口文件即要运行的文件，例如文件m1.py
**在入口文件中可以使用绝对导入**
	

入口文件也要以使用相对导入
	from .Bpack import m3，但不能使用python m1.py 
	**需要进入Tree目录后 使用python -m Tree.m1 来运行**
	执行指令中的-m是为了让Python预先import你要的package或module给你，然后再执行script。

即不把m1.py当作运行入口文件，而是也把它当作被导入的模块，这就和非运行入口文件有一样的表现了

	python m1.py   此时m1模块属于顶层模块

### py2与py3

py2默认为相对导入，py3默认为绝对导入。

如果py2要默认绝对导入，要在文件开头加入如下语句

```python
from __future__ import absolute_import 
# 意思是禁用了默认的隐式相对导入，但不会禁掉显式的相对导入。
```



## 包

### 定义

1， 定义：模块组成的集合

包即是一个文件夹，里面须有一个文件：——init——.py


> from A import *   叫模糊导入，
> 包的模糊导入由 ——all——定义决定

2， 导入包的本质：就是执行包下面的——init——.py文件。

3，虽然——init——.py文件可以在被动或者主动运行，但只有当文件主动import 包名或者from 包名 import * 时，——init——py里面的的import操作产生的对象才会被转移到此文件,但是会被——all——限制。

4,

```python
import A 
import A.amodule
from A import amodule 
from A import * 
# 其中 A为包名， amodule为包内的一个模块。
```

以上四句在执行时都会运行包内的——init——py文件，但是最后一句带星号的不能放在函数内执行。



假如包名字为A，包内有文件a.py 和 b.py ，如果要使用from A import * 来导入a和b文件里面的变量，那么——init——.py要这样做：

1，使用from .a import  *  导入a模块里面的变量

2， 使用from .b import * 导入b模块里面的变量

3， 使用 ——all—— = 【】   在【】中写入你所限制导入的变量  

​	如果【】为空，则限制所有变量的导入； 

​	如果不写——all——，那么将导入所有的变量。





### 导入的规则

* Python是根据——name——来决定一个模块在包中的结构

* 如果——name——是——main——，则它是顶层模块，没有包结构，也就找不到他的相对路径。
* 如果一个模块被直接运行，则它自己为顶层模块，它的——name——就是——main——

导入的基本规则如下：

如果是绝对导入，一个模块只能导入自身的子模块或和它的顶层模块同级别的模块及其子模块
如果是相对导入，一个模块必须有包结构且只能导入它的顶层模块内部的模块





### 相对导入

#### 优点

可以避免硬编码带来的维护问题； 例如我们修改了某一顶层的名，那么其子包所有的导入就不能用了。但是存在相对导入语句的模块，不能直接运行，否则会有异常。

绝对导入的优点：可以避免导入子包覆盖掉标准库模块（由于名字相同，发生冲突）。

#### 最好的文件结构

```python
project

​	【Dir1】（顶层）
​			【A】
​				a.py（不能调用超过Dir1范围的模块）
​			【B】 
​				b.py
​			【Log】
​				log.py
​	【Log_file】 （顶层）
​			log.log
​	main.py(它可以调用包A和包B的内容)（顶层）
```



#### 相对导入注意

只能用from 。。import 。。



#### 形式

**。 表示当前目录，就是本模块所在的目录**。

from . import xxx  导入和自己同目录下的模块
​from .packname import xxx  导入和自己同目录的包的模块 （低一层级，子目录里面）

from .. import module_name 导入上级目录的模块（高一层级，父目录里面）

from ..packname import xxx  导入位于上级目录下的包的模块 每多一个点就多往上一层目录（相同层级，兄弟目录里面）

from关键字是导入模块或者包的一部分；



### 绝对导入

1 import 只能导入模块，而不能导入模块中的对象（类、函数、变量）。例如可以import  A （模块），而不能import A.getName()   只能 用此形式 from A import getName 

2, 每个模块的Local名字空间都是独立的。对于本模块导入A模块，A模块又导入B模块，那么本模块import A 只能访问A模块，而不能访问B模块。虽然B模块已经加载到内存里面了。

#### 形式

1， 绝对导入的形式是 import A 、from A import B ;  特点就是不带“点”号。



问题

1， 同一个目录里面的两个py文件，一个import另一个，这种现象不存在相对导入还是绝对导入的问题。

2， 导入标准库，不存在相对导入还是绝对导入的问题。

3，相对导入和绝对导入仅适用于包内。  —— 这句话的意思是，一个目录只有是包了，它下面的文件的导入才区分相对或者绝对？





## 命名空间

​	每个模块都有自己的命名空间叫global  namespace  
​	每个函数都有自己的命名空间叫local namespace
​		记录模块的变量
​			包括functions、clesses、导入的modules、module级别的变量和常量
​	3，build-in namespace  内建空间
​	

locals（）与globals（）返回一个字典
	区别：前者是只读，后者是可写
	

## 运行文件

python -m  命令出现的错误：
	ModuleNotFoundError: __path__ attribute not found 
	如上面的命令所示，Python -m指的是把这个.py文件当做模块运行，但如果你一不小心加了.py这个后缀，就会出现这个错误。

	解决办法：
	1. 其实你要么把"-m"删除，
	2. 要么删除".py"后缀，问题就迎刃而解了
	采用的是2方法，再也没有报错。





## 其它

BASE_DIR = os.path.dirname(os.path.abspath(__file__))   
sys.path.append(BASE_DIR)



import sys 
sys.modules
	是一个字典；
	

在一个文件内的模块可以用相对导入
导入上级模块和相邻文件夹里面的模块可以用绝对导入,绝对导入以入口文件所在文件夹为起点.
记住:绝对导入以入口文件为起点,这个起点不要经常改变.