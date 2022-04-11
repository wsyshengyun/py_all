# coding:utf8

import project.base.miaoshufu2 as model


class LineItem:
    description = model.NonBlank()
    weight = model.Quantity()
    price = model.Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


lineitem = LineItem('111', 200, 2)
print(lineitem.subtotal())
