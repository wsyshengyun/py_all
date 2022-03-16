# coding:utf-8  
""" 使用type创建一个带有类属性的类 """
FatBoss = type("FatBoss", (), {'a':'wsy'})
print(FatBoss)
print(FatBoss.a)
# print(help(FatBoss))


""" type： 创建一个带有方法的类  """
def sell(self):
    print(self.hobby)

print('='*20)
FatBossGril = type("FatBossGril", (), {"hobby":"nihao", "sell":sell})
print(hasattr(FatBossGril, "sell"))
print(hasattr(FatBossGril, "hobby"))
fatobj = FatBossGril() 
fatobj.sell() 


""" 设置静态方法 """
@staticmethod
def static_method():
    print("static method...")

print("#" * 50)
FatBossa = type("Fatbossa", (), {"static_method":static_method})
print(FatBossa.static_method)
print(FatBossa.static_method())
