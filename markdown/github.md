##  一些名词
pull requests 
Issues 问题 
Marketplace  Marketplace市场
Explore 探索 
    推送你感兴趣的项目

forks：复刻

## 搜索技巧
介绍的比较详细的一个网址，在知乎上面：https://zhuanlan.zhihu.com/p/347723938

格式： in: name XXX(name 是什么？) starts: > XXX 

范围：  
### 使用用户名
author:biaochenxuying 匹配@biaochenxuying创作的提交
### in name 
in:name xxx // 按照项目（仓库）名搜索
### readme
in:readme xxx // 按照README搜索
### description
in:description xxx // 按照description搜索
### start
stars:>xxx // stars数大于xxx
### forks 
forks:>3000 // forks数大于xxx
### language
language:xxx // 编程语言是xxx
vue language:javascript配置具有`vue`字样、以javascript编写的仓库；
### pushed date
pushed:>YYYY-MM-DD // 最后更新时间大于YYYY-MM-DD

### 日期：
仓库的创建日期小于“一个日期”  
vue created:<2020-01-01

### 使用可视界面搜索
https://github.com/search/advanced
### 排除
名字排除：hello NOT world 匹配“hello”字样但不包含“world”字样的仓库。  
vue stars:>10 -language:javascript --> 匹配含有“vue”字样，有超过10个星号但并非以Javascript编写的仓库。  
> 另外，对带有空格的查询使用引号
cats NoT "hello world"

### 我探索的一些例子
in:description learn stars:>200  language:python 
> 在描述文字里含有learn字 且stars大于200 且语言是python的仓库。

