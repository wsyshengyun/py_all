## sys
### sys.argv
是一个列表, 列表里面全部是字符串对象
当在命令行运行一个py文件时 

方式1 python name.py  2
那么sys.argv的第一个元素是文件名 "name.py" 第二个元素是 '2'

方式2 python -m name.py 2 
那么sys.argv的第一个元素是 "-m", 第二个元素是 '2'

如果参数不是2 是a=1,那么第二个元素是"a=1"

### 循环
for .. else 和 while ..else 
意思是 正常运行循环体的内容, 然后再运行else后面的内容;
如果for或者while里面的break语句执行, 则 不在运行else后面的内容

