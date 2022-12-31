# coding:utf8

"""
描述符属性必须有一个名字属性吗, 用来区分不同的描述符?

有描述符属性的类在实例化时:
有几个描述符属性在实例化初就会调用几次__set__方法;

每个描述符必有一个属性, 这个属性A的值是一个字符串;
这个属性A,也即是主子的属性(被描述符参与的属性)的别名,即在__dict__的键;

"""


# 数量
class Quantity(object):
    def __init__(self, name):
        self.storage_name = name   # 存储名字

    def __get__(self, instance, owner):
        """ owner 为instance的类"""
        # return getattr(instance, self.storage_name) # 递归错误
        #     instance 是描述符的主的实例; LineItem()
        #     owner 是描述符的主 LineItem
        #     isinstance(instance, owner) => True
        return instance.__dict__.get(self.storage_name)

    def __set__(self, instance, value):
        print("QuAntity __set__ ->  instance :{0}, value is {1}".format(instance, value))

        if value > 0:
            instance.__dict__[self.storage_name] = value
        else:
            raise (ValueError(" value must be > 0"))



class LineItem(object):
    weight = Quantity("weight")
        # "weight" 就是描述符的 storage_name属性
    price = Quantity("price")

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price
    # 小计
    def subtotal(self):
        return self.weight * self.price

    def set_price(self, value=2):
        self.price = value




if __name__ == '__main__':
    truff = LineItem('Whit0 truffle', 100, 1)
    truff.weight = 10

    truff.set_price(value=4)
    print("subtotao is {}".format(truff.subtotal()))
    print('current price is {}'.format(truff.price))
    print("truff is :{}".format(truff))
    print("truff.__dict__: {}".format(truff.__dict__))
#         三个属性,就有三个元素



