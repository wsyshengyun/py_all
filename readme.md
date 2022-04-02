# python

## 单元测试

单元测试可以有效地测试某个程序模块的行为，是未来重构代码的信心保证。
单元测试的测试用例要覆盖常用的输入组合、边界条件和异常。
单元测试代码要非常简单，如果测试代码太复杂，那么测试代码本身就可能有bug。
单元测试通过了并不意味着程序就没有bug了，但是不通过程序肯定有bug。

## xpath

3.2 xpath的用法
xpath() 作用 提取页面数据,返回的是一个列表;
xpath的使用一定是建立在etree.HTML()之后的内容中;

xpath是如何提取页面数据的?
答:使用路径表达式

3.2.1 两种
第一种:/ 代表一层层的查找,如果/存在于开头,代表根路径.
bookstores = html.xpath('/html/body/bookstore')

第二种 // 任意路径 焦点在元素身上;  
html.xpath('//bookstore')

可以 一与二结合
html.xpath('//bookstore/book')

3.2.2 /text() 获取标签之间的内容
1, 找到所有title标签
2, 获取内容

title = html.xpath('//book/title/text())

3.3 位于 使用[] 可以理解为条件
3.3.1 [n] 代表第n个元素,n是数字 n>=1
获取第二个title元素
html.xpath('//book[2]/title/text()')
thml.xpath('//title[2]/text()')

last() 获取最后一个
last() - 1 获取倒数第二个

获取最后一本书的title标签之间的内容
html.xpath('//book[last()]/title/text()')

3.3.2 position() 位置/范围
支持 >   /   <  /  = /  >=  / <=  / !=

例如  获取最后两本书的title标签之间的内容  
步骤:
1, 先获取最后两本书  
2, 获取内容  
title = html.xpath('//book[posittion()>3]/title/text()')
title = html.xpath('//book[position() > last()-2]/title/text()')

3.3.3 获取属性名 @属性名
获取lang属性值为cng的title标签内容
html.xpath('//book/title[@lang='cng']/text()')

获取包含src属性的title标签内容
html.xpath('//book/title[@src]/text()')

获取包含属性的title标签的内容  
title = html.xpath('//book/title[@*]/text()')

获取最后一个title标签的src属性的值
html.xpath('//book[last()]/title/@src')

获取所有包含src属性的标签之间的内容
html.xpath('//*[@src]/text()')

3.4 and 与  连接的是谓语(条件)

html.xpath('//book/title[@lang='dng' and @class="t1"]/text()')
html.xpath('//book/title[@lang='dng'][@class="t1"]/text()')

3.5 or 或
html.xpath('//book/title[@lang='cng' or @lang="bng"]/text()')

3.6 | 连接路径
获取所有title标签和price标签之间的内容
html.xpath('//title/text() | //price/text()')

3.8 parse()
从文中读取数据
读取的文件,必须满足xml格式;
content = etree.pase('test.html')
res = etree.tostring(content, encoding='utf-8')
res.decode()
