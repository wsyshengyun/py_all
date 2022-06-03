
## pymongo


## Windows上使用MongoDB

## 环境搭建
安装 
pip install pymongo 
### 创建一个数据库
创建数据库需要使用 MongoClient 对象，并且指定连接的 URL 地址和要创建的数据库名。

### 连接数据库

from pymongo import  **MongoClient**

client = MongoClient(host='**localhost**', port=**27017**) 
db = client.test
collection = db.students
colper = db.person

### 判断数据库是否存在


## 一些函数

update_one (filter, update,....)

update_many  

delete_one(filter, collection=None, session=None) 

delete_many(...)  

db.test.count_documents({‘x’:1})



###一些条件

$inc  增加  ;  {‘$inc’: {‘x’:3}}   x的数据增加3  



 





## Linux 上使用 MongoDB

### 判断是否启动

pgrep mongo -l。

### 启动MongoDB

命令:sudo service mongodb start。

### 关闭MongoDB

命令:sudo service mongodb stop。

### 查看MongoDB的安装位置

命名：locate mongo

### 认mongodb 配置文件

存放在 sudo vim /etc/mongodb.conf。

### 卸载MOngoDB命令

sudo apt-get --purge remove mongodb mongodb-clients mongodb-server

### 启动MongoDB并将其添加为在启动时启动的服务：

systemctl start mongod
systemctl enable mongod

## Ubuntu安装2

ubuntu18.4安装MongoDB、启动、配置
原创X_watson 最后发布于2018-08-24 12:52:08 阅读数 3924  收藏
展开
第1步： 导入公钥

sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5

第2步：创建源列表文件MongoDB

echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.6 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.6.list

第3步：更新存储库

sudo apt-get update

第4步 ：安装MongoDB

sudo apt-get install -y mongodb-org

第5步：启动MongoDB并将其添加为在启动时启动的服务：

systemctl start mongod
systemctl enable mongod

第一次启动报错：

(dev) a@ubuntu:~$ systemctl start mongod
Failed to start mongod.service: Unit mongod.service not found.
(dev) a@ubuntu:~$ sudo systemctl start mongodb
Failed to start mongodb.service: Unit mongodb.service not found.
需要配置一下：

### 1、创建配置文件：

sudo nano /etc/systemd/system/mongodb.service

### 2.在里面追加文本，并按ctrl+X退出

[Unit]

Description=High-performance, schema-free document-oriented database

After=network.target

[Service]

User=mongodb

ExecStart=/usr/bin/mongod --quiet --config /etc/mongod.conf

[Install]

WantedBy=multi-user.target

### 3.启动服务，查看服务状态

sudo systemctl start mongodb

sudo systemctl status mongodb
显示如下信息，表示启动成功：

● mongodb.service - High-performance, schema-free document-oriented database
   Loaded: loaded (/etc/systemd/system/mongodb.service; disabled; vendor preset:
   Active: active (running) since Fri 2018-08-24 12:39:21 HKT; 11s ago
 Main PID: 21684 (mongod)
    Tasks: 19 (limit: 7054)
   CGroup: /system.slice/mongodb.service
           └─21684 /usr/bin/mongod --quiet --config /etc/mongod.conf

Aug 24 12:39:21 ubuntu systemd[1]: Started High-performance, schema-free documen

### 4.让它永久启动

sudo systemctl enable mongodb


