# flask学习

## 如何学习flask？

了解它的框架，把它分为几个部分，以及要知道这几个部分的相互关系，和对应的代码树结构；
几个部分；即蓝图、视图、业务、模板、配置、表form
> 配置是给哪些内容配置？

> 模板与视图函数
> 视图函数返回的就是模板的应用，首先视图函数要给模板传递“参数”（变量？）

> 业务？
> 业务即是把客户端发来的数据存储起来，以及服务器在需要的时候向数据库提取数据。

## 有哪些内容？

### 一些关键词

视图
业务
蓝图
路由
重定向
url
模板

### 什么是视图呢?

视图就是函数返回给客户端的url页面，一个页面就是一个视图；在服务器端，对应着的是路由url和url所对应的响应函数也即视图函数。
视图函数是需要注册的

### 什么是业务?

业务即是与数据库打交道的内容  
常见的数据库有哪些？  
Mysql、Mongdb、sqlite3

## 模板Jinja2

模板的渲染：读取字典和对象、条件控制语句、循环控制语句  
模板的继承：父文件使用block定义  
**父文件-基模板**

```python
{% block head %}
    内容。。。
    # 这个head要在子文件中引用；
{% endblock %}  
```

所以在基模板中有大量的块定义，以及块的嵌套定义，以便在衍生模板中实现块的内容，替换掉基模板中的块；

**子文件-衍生模板**
使用模块的继承需要与块相结合；父文件的里面要有块定义；继承的的使用结构是在子文件中添加如下:

```python
{%extends 'base.html'%}  # 这是在子文件的开头添加， ‘base.html’是父文件；
...
...
{% block head %} # 这里替换父文件里面的head
    ...
    ...
{% endblock %}
```

#### 使用模板要引入哪些扩展，如何使用这些包？

- Bootstrap

	pip install flask-bootstrap

## Web表单

#### 表单是什么？

#### 使用表单功能需要引入什么扩展？如何导入扩展的内容？

安装Flask-WTF扩展，pip install flask-wft 

设置密钥以防止跨站请求伪造的攻击：app.config['SECTET_KEY'] = 'hard to guess string'

```python
# 导入flask-wtf扩展
from flask.ext.wtf import Form #导入基类
from wtforms import StringField,SubmitField #字段
from wtforms.validators import Required #验证函数
```

> 关于验证
>
> StringField('what is your name?', validators=[Required()],validators指定了一个由验证函数组成的列表，在接受用户数据之前验证数据。

> 基类Form - 字段 - 验证字段
>
> 每个字段都用对象表示，字段对象可附属一个多个验证函数。

#### 如何使用表单？



## 蓝图

Blueprint（名字，名字，模板）
app = Flask（名字， 模板目录）

## 其它

http://localhost:5000/ 等效于 http://127.0.0.1:5000/

所需要的模块  

​	python-dotenv   #在项目的根目录下创建一个.flaskenv的文件，可以在里面输入FLASK_APP=microblog.py 就可以不用每次打开终端输入set ...了。

数据库模块  flask-sqlalchemy 

pip install flask_sqlalchemy  #from flask_sqlalchemy import SQLAlchemy 

pip install flask_migrate    # from flask_migrate import Migrate 

pip install python_dotenv  #



在gitbash下打开交互python，winpty  python



目前用的比较多的头像源是下面4个：

极客族CDN：https://sdn.geekzu.org/
七牛Gravatar：https://dn-qiniu-avatar.qbox.me/
V2EX：https://cdn.v2ex.com/gravatar/
LOLI：https://gravatar.loli.net/avatar/



------



from flask_avatars import Avatars

app = Flask(__name__)
avatars = Avatars(app)

pip install flask-avatars
默认头像
Flask-Avatars内置了几个默认头像，可以用来作为用户注册后的初始头像，或是作为博客评论者的头像。在模板中调用avatars.default()即可获取URL：

<img src="{{ avatars.default() }}">

------

模板文件必须要有一个文件夹，名字叫templates；而且视图函数要与templates同级；

------

关于JinJa2的注释问题

单行注释： {#...#}

多行注释：

{#

......

#}



------

出现的问题：虚拟环境已经下载了某个库，结果在运行的时候出现no mould named XXX; 

原因是虚拟环境没有激活。



------

pip install flask-moment

pip install flask-mail 

pip install pyjwt 安全令牌

------

按照预定的行为，当安装了 python-dotenv，Flask 会自动加载 .env 和 .flaskenv 里的环境变量。python-dotenv 在搜索存储环境变量的文件时，会从当前目录开始向上搜索，如果找到就返回对应的文件路径。但是这时 Flask 如果发现 .env 或 .flaskenv 的所在目录不是当前目录，就会把当前工作目录切换到 .env 和 .flaskenv 所在的目录（相关源码）。而如果你的程序模块或程序包不是和 .env/.flaskenv 同级目录的话，就会导致找不到程序实例。



怎么办：安装python dotenv包，在项目根文件夹中创建一个.flaskenv文件，然后添加，例如：

```
FLASK_APP=app.py (or whatever you named it)
FLASK_ENV=development (or production)
```



.flaskenv文件 中 # 号是注释



------

$ cp ../flask-mega-tutorial/microblog/app/templates/email/ app/templates/email/ -r

> 复制一个目录下的所有文件到另一个目录下面



pip freeze  > requirements.txt

pip install -r requirements.txt



os.environ是一个字典，严格的来说是像是一个字典，字典的键值是环境变量的名称，比如环境变量有Path，OneDrive， 键值为环境变量的值，它们全部是字符串的类型，如果有多个，就用分号-；隔开。

键不区分大小写；

os.getenv('path') == os.environ.get('path')







## flask应用的结构

一层目录里有app目录、config.py、blog.py、env目录、.gitinore文件
其中app目录里面有如下文件：  
templates目录、 __init__.py文件、 forms.py、routes.py
templates目录里放有一些html文件，是模板文件  
forms.py是表单文件；  
routes.py是视图文件，里面定义的各个路由函数；  



**flask的运行方式**

1, 在命令行输入flask run 

> 前提是先设置环境变量，如果是在windows上在命令行上输入：set FLASK_APP = 'microblog.py'
>
> 如果是在linux系统上将set换成export（出口n 输出vt）
>
> 另外安装python-dotenv 模块  #在项目的根目录下创建一个.flaskenv的文件，可以在里面输入FLASK_APP=microblog.py 就可以不用每次打开终端输入set ...了。

2, python blog.py   运行文件  

> 默认的网址就是127.0.0.1:5000 

## microblog

### db

数据的迁移  flask db migate -m "..."

把改变应用到数据库文件里面 flask db upgrade 

回滚上次的迁移  flask db downgrade 



打开flask的shell

> $ flask shell 



### 第五章 用户登陆

安装模块  pip install flask_login

已知 from flask import request; from werkzeug.urls import url_parse 



if not next_page 如何理解？

next_page = request.args.get('next')?

url_parse（next_page)此函数的作用是什么？





##　如何开始flask

1，创建一个目录

2，初始化git,设置.gitignore忽略文件

步骤如下：

- git init demo 
- touch .gitignore 

在.gitignore里面输入一些要忽略的文件的名称。

### 虚拟环境的建立

3，进入目录建立一个python虚拟环境

> 关于python环境的说明
>
> 有两个工具一个是pyenv另一个是virtualenv；pyenv是关于python版本的管理工具，有了它可以方便的切换系统python的版本，你就不需要同时安装多个python版本了。
>
> virtualenv是一个用来创建完成隔离的python虚拟环境的工具。注意是虚拟环境，再注意说的是环境，这个环境由不同的python包所构成。可以为每个项目创建一套独立的python环境，从而解决了不同工程对python包或者版本的依赖问题。

#### 创建虚拟环境的步骤

	- python -m venv .venv # 后面的.venv是虚拟环境的目录名字，自定义的。
	- 激活虚拟环境，在gitbash下输入命令 source .venv/Scripts/activate 
	- 退出虚拟环境 输入命令 deactivate 

#### 升级pip

python -m pip install --upgrade pip 

> 一定要加上pip -m 不然为升级失败的。





4，安装所需要的包：如下

	- flask 

### 建立一个目录结构

大型程序的目录结构示范

```python
app/
	__init__.py
	email.py
	models.py
	main/
		__init__.py
		errors.py
		forms.py
		views.py
	
	static/
		favicon.ico
	templates/
		404.html
		500.html
		base.html
		index.html
		user.html
		mail/
			new_user.html

config.py
manage.py # 入口模块，调用config.py
			# call app/__init__.py的工厂函数
migrations/
	alembic.ini
	env.py
	README
	script.py.mako
	versions
readme.md
requirements.txt # 安装所需要的python包
tests/
	__init__.py
	test_basics.py

```





l