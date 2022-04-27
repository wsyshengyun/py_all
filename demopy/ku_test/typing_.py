# coding:utf8
from typing import List, Dict, Tuple

vector = List[float]
var: vector = [1.1, 2.2]
var1: List[float] = [1.1, 2.2]
var2: vector = [1, 2, 3]
print(var2)
var3: vector = ['a', 'b']  # 警告, 但不会报错
print(var3)

vector_list_es = List[float]
vector_dict = Dict[str, vector_list_es]
vector_list = List[vector_dict]
# 等价于
vector_list_ex = List[Dict[str, List[float]]]


# 函数
def scale(scale: float, vector: vector_list) -> vector_list:
    for item in vector:
        for key, value in item.items():
            item[key] = [scale * num for num in value]
    print(vector)
    return vector


scale(2.2, [{"a": [1, 3, 3]}, {'b': [4, 5, 6]}])

# 更接近实际的例子
ConnectionOptions = Dict[str, str]
Address = Tuple[str, int]
Server = Tuple[Address, ConnectionOptions]


def broadcast_message(message: str, server: Server) -> None:
    print(message, server)


message = "发送服务器消息"
server = (("127.0.0.1", 127), {'name': '服务器1'})
broadcast_message(message, server)
