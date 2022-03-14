# coding:utf8


class abc:
    def __init__(self):
        print('at abc __init__')
        pass
        
    def printall(self):
        pass  





class Nihao:
    def __init__(self):
        self.a = 1
        print('at __init__  在吗')
        pass


    def __new__(cls, *args, **kwargs):
        print('at in __new__') 
        cls.b = 10
        return object.__new__(cls, *args, **kwargs)

    def __len__(self):
        return 100
    
    def __repr__(self):
        return "repr"

    def __str__(self):
        return "str.."

    def __del__(self):
        print("__del__")



obj = Nihao()
print(obj.b)
print("obj 的长度为 {}".format(len(obj)))
print("打印对象: {}".format(obj))
obj = 11 
print("obj 已经改变")

'''

class testDic(dict):
    def __setitem__(self, name, value):
        self.update((name: "value is %s " % str(value))

            
testobj = testDic() 
testobj('a')=100
print(testobj)

'''







