## 库

代理  fake_useragent  

## 命令行

### 创建一个项目

scrapy startproject tutorial

新建一个模板 
scrapy genspider [spider名称] [爬取网址]

更改settings
1, 不遵守robots协议
设置请求头
添加header并取消注释 


### 运行一个项目

scrapy crawl [spider名称] 
	加上--nlog可以不打印日志文件 
	scrapy crawl baidu_spider --nolog



### SHELL 命令

为全局命令。全局命令有7个，分别说明如下。　

startproject：创建项目。　

settings：查看设置信息。　

runspider：运行爬虫。　

shell：打开Shell调试。　

fetch：下载网页信息。　

view：使用浏览器打开指定网址。

version：查看版本号。





项目命令有7个，分别说明如下。　

crawl：运行指定的爬虫。　

check：检查爬虫代码。　

list：列出所有的爬虫。　

edit：使用默认的编辑器编辑爬虫文件。　

parse：使用爬虫抓取指定的URL。　

genspider：创建爬虫。　

bench：快速的性能测试。



genspider可以使用的模板有4个：　basic　crawl　csvfeed　xmlfeedbasic为基本爬虫模板，crawl模板生成继承CrawlSpider爬虫类的Spider，csvfeed、xmlfeed分别生成继承CSVFeedSpider与XMLFeedSpider爬虫类的Spider，后面章节会讲到除basic以外的其余3种通用爬虫。本小节使用crawl模板创建爬虫。

## 目录结构

项目目录/
	项目名称/
		spiders/
			spiders.py
		items.py
		middlewares.py   (也有项目没有中间件)
		pipelines.py
		settings.py 
	scrapy.cfg

### middlewares.py  中间件



settings设置

```
DOWNLOADERMIDDLEWARES = {
    'myproject.middlewares.Custom_A_DownloaderMiddleware': 543,
    'myproject.middlewares.Custom_B_DownloaderMiddleware': 643,
    'myproject.middlewares.Custom_B_DownloaderMiddleware': None,
}
数字越小，越靠近引擎，数字越大越靠近下载器，所以数字越小的，processrequest()优先处理；数字越大的，process_response()优先处理；若需要关闭某个中间件直接设为None即可
```

#### 下载中间件

```
process_request(request, spider)

进行一个request时,这个方法被调用,
返回
1,None(通常)

2,Response对象

3,Request对象

4,抛出IgnoreRequest异常



process_response(request,response,spider)

process_exception(request,exception, spider)
```



#### 爬虫中间件

```
	process_spider_input(response, spider)

当response通过spider时,这个方法调用

	process_spider_output(response, result, spider)

当spider返回result时,这个方法被调用

	process_spider_exception(response,exception, spider)

当spider抛出异常时这个中间件被调用
```



#### 代理

库

> ​	fake_useragent 
>
> form fake_useragent import UserAgent
>
> ua = UserAgent()
>
> ua.random()
>
> request.headers.setdefault('User-Agent', ua.random())
>
> request.headers['User-Agent'] = ua.random() 
>
> 
>
> ku2
>
> ​	user_agent 
>
> from user_agent import agents 
>
> agent = agents.random.choice(agents)





### settings.py

BOT_NAME = 'nextSpider' 
spider_modules = [] 
newspider_module = '' 

robotstxt_obey = true 

#### 日志

LOG_FILE = './log.log'
LOG_ENABLED = True 
LOG_ENCODING = 'utf-8'
LOG_LEVEL = 'DEBUG'



#### export导出设置

FEED_FORMAT = 'csv'
FEED_EXPORT_ENCODING = 'gbk'
FEED_EXPORT_FIELDS=['book_name', 'price', 'stock_num', 'reviews_num']
FEED_URI = 'export_data/%(name)s.csv'

​	产生一个export_data的目录

​	name为爬虫的名字



#### filedown

ITEM_PIPELINES = {

​	'scrapy.pipelines.files.FilesPipeline':1

}

FILES_STORE = 'example_src'

#### mongodb

MONGO_DB = 'BD_news'

MONGO_HOST = '127.0.0.1'

MONGO_PORT = 27017

### 管道 

类定义 class NextspiderPipeline(object):

​	; 不必继承,只要定义了下面的函数就可以了

def process_item(self, item, spider):
		return item 

​		raise DropItem('')   Item项目不在传递下去,以及保存到数据库

def process_item(self, item, spider) 
def open_spider(self, spider) 
def close_spider(self, spider) 



### 爬虫  scrapy.Spider类 

from scrapy.http import Request 

功能
	start_requests() 
	parse() 
属性:
	name 
	allowed_domains = [] 
	start_urls = []  ; 开始爬取数据的URL列表
	
	

#### Request

参数:url, meta = {}, callback = self.parse1 (调用别的解析函数)
属性:
	request.cookies = {} 
	request.headers['User-Agent'] = UserAgetn().random 
	request.meta['proxy'] = 'http://27.188.62.3:8086'
	
	
	

#### Response

response.meta['result'] 
从相对路径取得绝对路径
next_url = response.urljoin(next_url)



#### Selector(response)

`obj = Selector(response).xpath('body/div[@class="c" and @id]')`
response 也有 selector属性 
上面也可以写成  ojb = response.xpath(....)

构造一个Selector 
from scrapy.selector import Selector
text = '<a....</a>' 
sel = Selector(text=text) 
	selector会自动补全text的.补全后的是以html开头的
	
	
Selector对象或者SelectorList对象 
	extract()   返回一个列表
	extract_first()  ; SelectorList专有, 返回一个字符串
	re() 
	re_first()  ; SelectorList专有


```
xpath(...).extract_first()
xpath(...).extract()
```




#### xpath

/ 根节点  文档的根 

##### 文档的节点

根节点

元素节点 html/body/div/p/a

属性节点 href

文本节点 

##### 节点直接的关系

父子/兄弟/祖先和后裔



##### 基础语法

/ 选中文档的根节点

. 当前节点 即 X.xpath  X即当前节点

.. 父节点

E  选中子节点中所有的E节点  关键点:子节点

//E  选中后代节点的所有E节点

> //div[1] 第几个div节点

\*  选中所有元素的子节点 

@* 选中所有的属性节点

text() 选中所有的文本节点

> 理解一个节点
>
> 一个节点即是用开闭标签表示的内容包含开闭标签,比如<div>...</div> 
>
> 也包含文本节点 ,文本节点不带开闭符号 
>
> 选中节点  xpath('/html/body/div')
>
> 选中的是包含div的节点,

[]谓语

> [数字]
> [@属性名字]
> [@属性名字 = 属性值]
> [函数]
> 	[contians(@class, "str")]
> 	[last()]
> 	[position()<3]



#### css

​	例子1 	

response = '<div> class="toctree-wrapper compound"'...

css = div.toctree-wrapper.compound

​	语法

E  单个元素

e1,e2 选中两个元素

e1 e2 选中e2(e1的后代元素)

e1>e2 选中e2(e1的子元素,不是第一个)

e1+e2 选中e2(e1的兄弟元素)

.classname : e1.classname 选中属性包含classname的e1元素

#id : 选中ID为 id的元素

{attr}  选中包含attr属性的元素

{attr=value}  选中包含attr属性的元素,且值为value的元素.

{attr~=value}  选中含有属性attr且值包含value的元素

e:nth-child(n)  选中e元素,且该元素必须是其父元素的第n个元素.

e:empty  选中没有子元素的元素

e:text  选中e元素中的文本节点 

e::text   e中所有的文本节点  

div:first-child>a:last-child     选中第一个div的最后一个a元素(选中的是一个a元素)







#### yield

yield Request(...)

#### re 

re.findall(u'', text1) 

#### datetime

datetime.datetime.strptime(birthday[0], "%Y-%m-%d") 



### scrapy.cfg

[settings]
default = tutorial.settings 

[deploy] 
project = tutorial 


### 英语
category  种类, 类别

deploy 部署 展开


