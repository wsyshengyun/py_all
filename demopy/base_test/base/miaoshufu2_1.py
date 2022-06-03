# coding:utf8

from demopy.base_test.base import miaoshufu2 as model


class LineItem:
    description = model.NonBlank()  # 去掉空格
    weight = model.Quantity()  # 描述符 值不能小于零
    price = model.Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


lineitem = LineItem('111', 200, 2)
print(lineitem.subtotal())
