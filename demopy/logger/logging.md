## 





































## 其它相关

### 禁止输出

logging.disable(logging.INFO)

logger.disabled = True

### basicConfig

datefmt = "%Y/%m%d  %H:%M:%S"

filename = '', 

format = ''

level = ''



## 几个重要的概念

Logger 记录器，暴露了应用程序代码能直接使用的接口。
Handler 处理器，将（记录器产生的）日志记录发送至合适的目的地。
Filter 过滤器，提供了更好的粒度控制，它可以决定输出哪些日志记录。
Formatter 格式化器，指明了最终输出中日志记录的布局。

### Logger 记录器

Logger是一个树形层级结构，在使用接口debug，info，warn，error，critical之前必须创建Logger实例，即创建一个记录器，如果没有显式的进行创建，则默认创建一个root logger，并应用默认的日志级别(WARN)，处理器Handler(StreamHandler，即将日志信息打印输出在标准输出上)，和格式化器Formatter(默认的格式即为第一个简单使用程序中输出的格式)。

创建方法: logger = logging.getLogger(logger_name)

创建Logger实例后，可以使用以下方法进行日志级别设置，增加处理器Handler。

logger.setLevel(logging.ERROR) # 设置日志级别为ERROR，即只有日志级别大于等于ERROR的日志才会输出
logger.addHandler(handler_name) # 为Logger实例增加一个处理器
logger.removeHandler(handler_name) # 为Logger实例删除一个处理器

### Handler 处理器

Handler处理器类型有很多种，比较常用的有三个，StreamHandler，FileHandler，NullHandler，详情可以访问Python logging.handlers

创建StreamHandler之后，可以通过使用以下方法设置日志级别，设置格式化器Formatter，增加或删除过滤器Filter。

ch.setLevel(logging.WARN) # 指定日志级别，低于WARN级别的日志将被忽略
ch.setFormatter(formatter_name) # 设置一个格式化器formatter
ch.addFilter(filter_name) # 增加一个过滤器，可以增加多个
ch.removeFilter(filter_name) # 删除一个过滤器
StreamHandler
创建方法: sh = logging.StreamHandler(stream=None)

FileHandler
创建方法: fh = logging.FileHandler(filename, mode='a', encoding=None, delay=False)

NullHandler
NullHandler类位于核心logging包，不做任何的格式化或者输出。
本质上它是个“什么都不做”的handler，由库开发者使用。

### Formatter 格式化器

使用Formatter对象设置日志信息最后的规则、结构和内容，默认的时间格式为%Y-%m-%d %H:%M:%S。

创建方法: formatter = logging.Formatter(fmt=None, datefmt=None)

其中，fmt是消息的格式化字符串，datefmt是日期字符串。如果不指明fmt，将使用'%(message)s'。如果不指明datefmt，将使用ISO8601日期格式。

Filter 过滤器
Handlers和Loggers可以使用Filters来完成比级别更复杂的过滤。Filter基类只允许特定Logger层次以下的事件。例如用‘A.B’初始化的Filter允许Logger ‘A.B’, ‘A.B.C’, ‘A.B.C.D’, ‘A.B.D’等记录的事件，logger‘A.BB’, ‘B.A.B’ 等就不行。 如果用空字符串来初始化，所有的事件都接受。

创建方法: filter = logging.Filter(name='')

### 以下是相关概念总结:

熟悉了这些概念之后，有另外一个比较重要的事情必须清楚，即Logger是一个树形层级结构;
Logger可以包含一个或多个Handler和Filter，即Logger与Handler或Fitler是一对多的关系;
一个Logger实例可以新增多个Handler，一个Handler可以新增多个格式化器或多个过滤器，而且日志级别将会继承。

element_relation.jpg

## Logging工作流程

### logging模块使用过程

第一次导入logging模块或使用reload函数重新导入logging模块，logging模块中的代码将被执行，这个过程中将产生logging日志系统的默认配置。
自定义配置(可选)。logging标准模块支持三种配置方式: dictConfig，fileConfig，listen。其中，dictConfig是通过一个字典进行配置Logger，Handler，Filter，Formatter；fileConfig则是通过一个文件进行配置；而listen则监听一个网络端口，通过接收网络数据来进行配置。当然，除了以上集体化配置外，也可以直接调用Logger，Handler等对象中的方法在代码中来显式配置。
使用logging模块的全局作用域中的getLogger函数来得到一个Logger对象实例(其参数即是一个字符串，表示Logger对象实例的名字，即通过该名字来得到相应的Logger对象实例)。
使用Logger对象中的debug，info，error，warn，critical等方法记录日志信息。

### logging模块处理流程

logging_flow.png
判断日志的等级是否大于Logger对象的等级，如果大于，则往下执行，否则，流程结束。
产生日志。第一步，判断是否有异常，如果有，则添加异常信息。第二步，处理日志记录方法(如debug，info等)中的占位符，即一般的字符串格式化处理。
使用注册到Logger对象中的Filters进行过滤。如果有多个过滤器，则依次过滤；只要有一个过滤器返回假，则过滤结束，且该日志信息将丢弃，不再处理，而处理流程也至此结束。否则，处理流程往下执行。
在当前Logger对象中查找Handlers，如果找不到任何Handler，则往上到该Logger对象的父Logger中查找；如果找到一个或多个Handler，则依次用Handler来处理日志信息。但在每个Handler处理日志信息过程中，会首先判断日志信息的等级是否大于该Handler的等级，如果大于，则往下执行(由Logger对象进入Handler对象中)，否则，处理流程结束。
执行Handler对象中的filter方法，该方法会依次执行注册到该Handler对象中的Filter。如果有一个Filter判断该日志信息为假，则此后的所有Filter都不再执行，而直接将该日志信息丢弃，处理流程结束。
使用Formatter类格式化最终的输出结果。 注：Formatter同上述第2步的字符串格式化不同，它会添加额外的信息，比如日志产生的时间，产生日志的源代码所在的源文件的路径等等。
真正地输出日志信息(到网络，文件，终端，邮件等)。至于输出到哪个目的地，由Handler的种类来决定。
注：以上内容摘抄自第三条参考资料，内容略有改动，转载特此声明。

### 再看日志配置

配置方式
显式创建记录器Logger、处理器Handler和格式化器Formatter，并进行相关设置；
通过简单方式进行配置，使用basicConfig()函数直接进行配置；
通过配置文件进行配置，使用fileConfig()函数读取配置文件；
通过配置字典进行配置，使用dictConfig()函数读取配置信息；
通过网络进行配置，使用listen()函数进行网络配置。

### basicConfig关键字参数

关键字	描述
filename	创建一个FileHandler，使用指定的文件名，而不是使用StreamHandler。
filemode	如果指明了文件名，指明打开文件的模式（如果没有指明filemode，默认为'a'）。
format	handler使用指明的格式化字符串。
datefmt	使用指明的日期／时间格式。
level	指明根logger的级别。
stream	使用指明的流来初始化StreamHandler。该参数与'filename'不兼容，如果两个都有，'stream'被忽略。
有用的format格式
格式	描述
%(levelno)s	打印日志级别的数值
%(levelname)s	打印日志级别名称
%(pathname)s	打印当前执行程序的路径
%(filename)s	打印当前执行程序名称
%(funcName)s	打印日志的当前函数
%(lineno)d	打印日志的当前行号
%(asctime)s	打印日志的时间
%(thread)d	打印线程id
%(threadName)s	打印线程名称
%(process)d	打印进程ID
%(message)s	打印日志信息
有用的datefmt格式
参考time.strftime

配置示例
显式配置
使用程序logger.py如下:

```
# -*- encoding:utf-8 -*-

import logging

# create logger

logger_name = "example"
logger = logging.getLogger(logger_name)
logger.setLevel(logging.DEBUG)

# create file handler

log_path = "./log.log"
fh = logging.FileHandler(log_path)
fh.setLevel(logging.WARN)

# create formatter

fmt = "%(asctime)-15s %(levelname)s %(filename)s %(lineno)d %(process)d %(message)s"
datefmt = "%a %d %b %Y %H:%M:%S"
formatter = logging.Formatter(fmt, datefmt)

# add handler and formatter to logger

fh.setFormatter(formatter)
logger.addHandler(fh)

# print log info

logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')```
```



##### 文件配置

配置文件logging.conf如下:
```[loggers]
keys=root,example01

[logger_root]
level=DEBUG
handlers=hand01,hand02

[logger_example01]
handlers=hand01,hand02
qualname=example01
propagate=0

[handlers]
keys=hand01,hand02

[handler_hand01]
class=StreamHandler
level=INFO
formatter=form02
args=(sys.stderr,)

[handler_hand02]
class=FileHandler
level=DEBUG
formatter=form01
args=('log.log', 'a')

[formatters]
keys=form01,form02

[formatter_form01]
format=%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s```

使用程序logger.py如下:
​```#!/usr/bin/python
# -*- encoding:utf-8 -*-
import logging
import logging.config

logging.config.fileConfig("./logging.conf")

# create logger
logger_name = "example"
logger = logging.getLogger(logger_name)

logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')```

##### 字典配置
有兴趣的童靴可以使用```logging.config.dictConfig(config)```编写一个示例程序发给我，以提供给我进行完善本文。

##### 监听配置
有兴趣的童靴可以使用```logging.config.listen(port=DEFAULT_LOGGING_CONFIG_PORT)```编写一个示例程序发给我，以提供给我进行完善本文。

更多详细内容参考[logging.config日志配置](http://python.usyiyi.cn/python_278/library/logging.config.html#module-logging.config)


```

## 日志文件按大小或者时间划分

功能所在的模块：logging.handles

所需要的类：TimedRotatingFileHandler、 RotatingFileHandler

它们都继承自基类：BaseRotatingHandler

### 大小

每隔1000 Byte划分为一个日志文件，备份文件为3个

file_handler = logging.handlers.RotatingFileHandler('test.log', mode='w', maxBytes=1000, backupCount=3,encoding='utf-8')

#### 字节

> byte 为字节  简写为B  1B即1节字  ，1字节是8位长的数据单位。
>
> 字节通常简写为B
>
> 位通常简写为b
>
> 1B（byte，字节） = 8bit
>
> 1KB（千字节）  = 1024B  = 2^10B  千字节
>
> 1MB = 1024KB = 2^20；百万字节
>
> 1GB = 1024MB = 2^30B 十亿字节
>
> 1TB = 2^40B  万亿字节
>
> 

### 时间

每隔一小时 划分一个日志文件，interval是时间间隔，备份文件为10个

handler2 = logging.handlers.TimedRotatingFileHandler('test.log', when='H', interval=1, backupCount=10)



## 进阶

如何按照进程或者线程划分为不同的日志文件，也即一个进程或者线程对应一个文件？？

级别  critical > error > warning >info >debug
debug 打印全部日志
info  打印 info及以上的日志
warning 意想不到的问题, 一些问题将在不久的时候发生
error  软件没能执行一些功能
critical   一个严重的错误, 程序无法正常运行 

## 基本应用

import logging 
logging.basicConfig(level=logging.NOTSET) 设置日志的级别
logging.debug(u"如果级别如上, 那么debug以上的都可以显示了")

日志级别
打印到、终端，指定文件；

多模块打印
	Logger -- 字符串名字 __name__
		-- 添加@句柄
		-- 设置等级　critical 50; error40 warning30 info20 debug 10 notset 0
			--- 开始执行输出
	@句柄 -- 文件路径 * logging.handlers.RotatingFileHandler(path)
					logging.FileHandler(path) 与上面的区别？？
		-- 设置@格式
	@格式 
		* %(asctime)s
		* levelname
		* message
		* thread 线程的ID
		×　threadName　ｓ　线程名字
		×　processName　ｓ　进程的名字
		×　module　ｓ　模块名称
		×　lineno　行号
		×　filename　程序名
		×　pathname　ｓ　执行的路径
		×　levelno　ｓ　日志级别的数值

logger.error('',exc_info=True)  # 详细的信息
RotatingFileHandler	
	logfile,maxBytes=100*1024*1024,
	backupCount=10    # 100M





名词解释1

```python
Logging.Formatter  日志的格式, 自定义了设置日期和时间
Logging.Logger    logging模块的主体 
	为程序提供记录日志的接口
	判断日志所处的级别, 并判断是否过滤
	根据级别, 将日志分给不同的handler
常用的函数
	Logger.setLevel()
	Logger.addHandler()   / removeHandler()
	Logger.addFilter()   添加一个Filter过滤器
	Logger.Handler: Handler基于日志级别对日志进行分发
	setLevel() 
	setFormatter()
输出到控制台
	logging.basicConfig(
		level=logging.DEBUG, 
		format="%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s)"
	)
	logging.info('....')
	logging.debug('....')
输出到文件
	import os.path
	import time 
	logger = logging.getLogger()  # 创建一个logger
	logger.setLevel(logging.INFO)  # Log等级总开关
	# 创建一个handler用于写入日志文件
		rq = time.strftime('%Y%m%d%H%M',  time.localtime(time.time()))
		log_path = os.path.dirname(os.getcwd()) + '/Logs/'
		log_name = log_path + rq + '.log'
		logfile = log_name
		fh = logging.FileHandler(logfile,  mode='w')
		fh.setLevel(logging.DEBUG)  # 输出到file的等级开关
	# 定义handler的输出格式
		formatter = logging.Formatter("(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
		fh.setFormatter(formatter)
	# 将logger添加到handler里面
		logger.addHandler(fh)
	# 日志
		logger.debug('....')
```


​	
​	

