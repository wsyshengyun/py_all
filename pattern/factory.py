# coding:utf8
"""
工厂模式
- 用户能扩展软件库或框架的内部组件
- 无法预知对象确切类别及其依赖关系
- 复用现有的对象来节省系统资源, 从而不用每次都重新创建对象.
"""

class CarFactory:
    @staticmethod
    def createcar(brand):
        if brand == "benchi":
            return BenChi()
        elif brand == "baoma":
            return Baoma()
        else:
            return Byd()
        

class BenChi:
    pass


class Baoma:
    pass


class Byd:
    pass


if __name__ == '__main__':
    factory = CarFactory() 
    car1 = factory.createcar("BYD")
    car2 = factory.createcar("baoma")
    print("Car1 车型为: {}".format(car1))
    print("car2 车型为: {}".format(car2))

