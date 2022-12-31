# coding:utf8

class QList(list):
    push_back = lambda self, v: self.append(v)
    def indexOf(self, v):
        return self.index(v) if v in self else -1

    push_front = lambda self,v: self.insert(0, v)
    size = lambda self:len(self )
    empty = lambda self: not len(self )


if __name__ == '__main__':
    obj = QList()
    obj.push_front(1)
    obj.push_front(11)
    obj.push_front(12)
    obj.push_front(14)
    print(obj)
    print(obj.size())
    print(obj.empty())
    print(obj.indexOf(11))
