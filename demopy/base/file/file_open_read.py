#encoding:utf8  

path = 'bb.bin'
txt = "你好，我是一个工人！"
txtb = txt.encode('gbk')
# print(txtb)
def write(txt):
    with open(path, 'wb') as f:
        print("要写入的文件内容是：%s" % txt)
        f.write(txt)
        print("文件写入完成.")

def read():
    with open(path, mode='rb') as fp:
        content = fp.read()
        print("读取到的文件内容是： %s" % content)
        print("读文件完成。")
        return content

def test():
    content = read()
    con_utf = content.decode('gbk')
    print(con_utf)

if __name__ == "__main__":
    test()
    # write(txtb)
    # read()


