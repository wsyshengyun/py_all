





## PYQT环境配置

- 安装pyqt5库

  pip install pyqt5 

  > pyqt5 仅支持py3.5以上的版本了。
  >
  > pip 要升级到版本 22， 版本19不能安装

- 安装qt designer

	> https://github.com/altendky/pyqt5-tools/releases/tag/v5.7.dev1
	>
	> 不支持pip安装，可以下载whl文件安装

- 安装pyUIC

	它可以把Qt Designer设计完所生成的UI文件，转换成py文件，是一个命令行工具

	命令是

	```python
	python -m PyQt5.uic.pyuic xxx.ui -o xxx.py   # 两个xxx的名字也可以不相同
	```



### 其他安装

> 1.sip的安装，在命令行窗口输入：
>
> pip install sip==4.19.17 -i https://pypi.douban.com/simple
>
> 2.PyQt5的安装，在命令行窗口输入：
>
> pip install PyQt5==5.10.1 -i https://pypi.douban.com/simple
>
> 3.QScintilla的安装，在命令行窗口输入：
>
> pip install QScintilla==2.10.2 -i https://pypi.douban.com/simple
>
> 4.pyqt5-tools的安装，在命令行窗口输入：
>
> pip install pyqt5-tools==5.10.1.1.3 -i https://pypi.douban.com/simple



### QtDesigner汉化

汉化文件名字：designer_zh_CN.qm 是简体中文
步骤3
将拷贝的翻译文件复制到 PyQt5 的translations文件夹中
笔者的路径：F:\Python\Lib\site-packages\PyQt5\Qt\translations

步骤4
将拷贝的翻译文件复制到 pyqt5-tools 的translations文件夹中
笔者的路径：F:\Python\Lib\site-packages\pyqt5-tools\translations
designer_zh_CN.qm是简体中文


### vscode安装扩展 

PYQT Integration



## 了解

### 类

**QtCore模块**涵盖了包的核心的非GUI功能，此模块被用于处理程序中涉及到的 time、文件、目录、数据类型、文本流、链接、mime、线程或进程等对象。

**QtGui模块**涵盖多种基本图形功能的类; 包括但不限于：窗口集、事件处理、2D图形、基本的图像和界面 和字体文本。

**QtWidgets模块**包含了一整套UI元素组件，用于建立符合系统风格的classic界面，非常方便，可以在安装时选择是否使用此功能。

**QtMultimedia模块**包含了一套类库，该类库被用于处理多媒体事件，通过调用API接口访问摄像头、语音设备、收发消息（radio functionality）等。

**QtBluetooth模块**包含了处理蓝牙活动的类库，它的功能包括：扫描设备、连接、交互等行为。

**QtNetwork模块**包含用于网络编程的类库，这组类程序通过提供便捷的TCP/IP 及 UDP 的 c/s 程式码集合，使得基于Qt的网络编程更容易。

**QtPositioning模块**用于获取位置信息，此模块允许使用多种方式达成定位，包括但不限于：卫星、无线网、文字信息。此应用一般用于网络地图定位系统。

**Enginio模块**用于构建客户端的应用程式库，用于在运行时访问 Qt Cloud 服务器托管的应用程序。

**QtWebSockets模块**包含了一组类程序，用以实现websocket协议。

**QtWebKit**包含了用于实现基于webkit2的网络浏览器的类库。

**QtWebKitWidgets模块**包含用于基于WebKit1的Web浏览器实现的类，用于基于QtWidgets的应用程序

**QtXml模块**包含了用于处理XML的类库，此模块为SAX和DOM API 的实现提供了方法。

**QtSvg模块**通过一组类，为显示矢量图形文件的内容提供了方法。

**QtSql模块**提供了数据库对象的接口以供使用

**QtTest模块**包含了可以通过单元测试，以调试PyQt5应用程式的功能。

## 

### PyQt5并不向下兼容PyQt4

，主要是由于其有几个较大的改变。虽不兼容，但是旧代码调整到新库并不是很难。它们的主要差异如下：

Python的模块已经重新构建，一些模块已经被放弃，如：QtScript。其他的模块被分割到一些子模块当中，如：QtGui，QtWebkit。
一些新的模块会推出，如：QtBluetooth，QtPositioning或Enginio。
PyQt5仅支持新型信号和插槽。对SIGNAL（）或SLOT（）的调用不再支持（这点很重要哦！）。





##  7个类 


1.QObject类

QObject类：所有PyQt对象的基类，换而言之是在PyQt中所有的类均继承自QObject，这使得QObject中的所有方法在其他类中可以使用，是PyQt对象模型的核心。


2.QPaintDevice类

QPaintDevice类：所有可绘制对象的基类


3.QApplication类

QApplication类：用于管理图形用户界面应用程序的控制流和主要设置，并且无论程序有多少个窗口，该类的实例化对象只有一个。QApplication继承自QGuiApplication类，并且添加了一些函数用来支持以QWidget基础组件，可以控制QWidget组件的初始化工作和收尾工作。


4.QMainWindows类

QMainWindows类：提供一个有菜单栏、停靠窗口和状态栏的主应用程序窗口 QMainWindow主窗口提供了一个应用程序框架，它有自己的布局,可以在布局中添加控件。


5.QWidget类

QWidget类：所有用户界面对象的基类（QDialog类和QFrame类都继承自QWidget类），所有的窗口或者控件都直接或者间接的继承自QWidget类。


6.QFrame类

QFrame类：有框架的窗口控件的基类，它也被用来直接创建没有任何内容的简单框架。 主要是用来控制一些边框样式，例如凸起、凹下、阴影、线宽等；继承自QWidget类。


7.QDialog类

QDialog类：对话框窗口类。对话框窗口是主要用于短时期任务以及用户进行简要通讯的顶级窗口，在PyQt5中定义了一系列的标准对话框类，让用户能够方便快捷地通过各个类完成字号大小，字体颜色以及文件的选择等，便于人机交互。
QDialog类的子类主要有QMessageBox，QFileDialog，QColorDialog，QFontDialog，QInputDialog等，主要是子类的应用。



## 具体的类



###  QColor类

 col = QColorDialog.getColor()的结果就是QColor类

col.name() 结果是一个十六进制的颜色值, #223344

col.isValid() = True

> QColorDialog为一个对话框窗体，当选择完成颜色后，点击确定按钮后，返回一个颜色对象QColor对象。

### QFont

> font, ok = QFontDialog.getFont()
> 	ok的值为True或者False
> 	True点击了字体对话框里面的OK按钮,False为点击了Cancel按钮   
> 	font为QFont类型

font的几个方法:

family()  返回字体的名称; 

weight() 返回字体的?属性 ,有的值为50

bold() 字体是否加粗

tostring()   字体的11个属性值以逗号分割 连在一起的字符串

familys()  没有此方法!

### QFileDialog

```python
   form pathlib import Path  # pathlib 库 关注
    home_dir = str(Path.home())
        # home_dir: c:/Users/w3986
    logger.info("home_dir = {}".format(home_dir))
    # fname = QFileDialog()
    fname = QFileDialog.getOpenFileName(self, 'Open file', home_dir ) 
        # 'Open file'为对话框标题
        # fname: 为一个元组, 2个元素,1:所选择的文件的完整路径; 2:文件过滤(文件类型)[All Files(*)])
        # 当点击对话框<取消>是返回一个空的元组("", ""))
  
    logger.info("fname = {}".format(fname))
```
### QInputDialog

```python
  def showDialog(self):
     text, ok = QInputDialog.getText(self, 'Input Dialog对话框标题', 'Enter your name: 一个标签的text')

```

### 总结1

QColorDialog.getColor()

​		返回的是一个颜色对象, 有IsValid和name方法

​		isValid 返回的是布尔值

​		name 是颜色值 #号开头.

QFontDialog.getFont()

​		返回的是一个元组,1:字体   2:布尔值  

QFileDialog.getOpenFileName(self, 对话框标题, 要打开的文件目录位置)

​		返回的是一个元组,1:文件的路径(字符串)  2文件的过滤(字符串)

QInputDialog.getText(self, 对话框标题, 标签控件的显示的文字)

​		返回都是一个元组,1:输入的字符串,  2:布尔值



### QCheckBox

PyQt5>QtCore>Qt>QChecked=2

QCheckBox的状态有两个值0和2; 0为未选中,2为选中

```
QCheckBox.toggle()  # 动作:与原来相反的状态
QCheckBox.stateChanged.connect(func) # 默认给func传递一个参数
```



### QProgressBar进度条
主要的函数是setValue(val),其中val是0到100的值 


### QSlider  滑块

### QBasicTimer

​      *定时器的名称  QBasicTimer  basic:基础的*

​      *方法有: is_Active()*  

​          *stop()* 

​          *start(100, self)  100指的是100毫秒,为定时器的间隔时间,到时间激活一下事件*

### QPixmap

QPixmap 是用于处理图像的小部件之一。它针对在屏幕上显示图像进行了优化。在我们的代码示例中，我们将使用 QPixmap 在窗口上显示图像。

### QLineEdit

QLineEdit 是一个允许输入和编辑单行纯文本的小部件。小部件具有撤消和重做、剪切和粘贴以及拖放功能。

### QSplitter

QSplitter 允许用户通过拖动子控件之间的边界来控制子控件的大小。在我们的示例中，我们展示了三个使用两个拆分器组织的 QFrame 小部件。

### QComboBox

QComboBox 是一个允许用户从选项列表中进行选择的小部件。



### Qrag 和 drop in PyQt5

最后修改于 2022 年 1 月 6 日
在 PyQt5 教程的这一部分中，我们将讨论拖放操作。
在计算机图形用户界面中，拖放是单击虚拟对象并将其拖动到不同位置或另一个虚拟对象上的动作（或支持该动作的动作）。一般来说，它可以用来调用多种动作，或者在两个抽象对象之间创建各种类型的关联。
拖放是图形用户界面的一部分。拖放操作使用户能够直观地做复杂的事情。
通常，我们可以拖放两件事：数据或一些图形对象。如果我们将图像从一个应用程序拖到另一个应用程序，我们拖放二进制数据。如果我们在 Firefox 中拖动一个选项卡并将其移动到另一个位置，我们就会拖放一个图形组件。



### QDrag



## 布局

QlineEdit控件



### 水平布局

在水平布局里面,控件的宽度是可以变化的,控件只能设置最小宽度,而不能设置固定的宽度.

### 垂直布局



### 表格布局



## 信号与槽

### 事件Events

事件主要由应用程序的用户生成。但它们也可以通过其他方式生成；例如Internet 连接、窗口管理器或计时器。当我们调用应用程序的 exec_ 方法时，应用程序进入主循环。主循环获取事件并将它们发送给对象





### 形式

控件——动作ed——connect——(函数名字)







## 解决问题

解决Nomodule named pyqt5.sip

[(36条消息) 解决No module named 'PyQt5.sip'_ceeko2012的博客-CSDN博客_pyqt5.sip](https://blog.csdn.net/ceeko2012/article/details/104598330)

