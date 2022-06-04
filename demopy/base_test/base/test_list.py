import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.L = [1, 2, 3, 4, 5]

    def test_create_list(self):
        """
        生成一个新的列表的方法
        1, 空列表 [] list()
        2, 有值的元素 [1, 2, 3, 4, 5]
        3, [None] * 2
        4, 列表推导式
        5, copy()
        """
        _equal = self.assertEqual

        L = []

        L1 = list()
        _equal(L, L1)

        L = [1, 2, 3, 4, 5]
        _equal(L, self.L)

        L = [None] * 2
        _equal(L, [None, None])
        L = [''] * 6
        _equal(len(L), 6)

        # 列表推导式
        l1 = [i for i in range(10)]
        l2 = [i for i in range(10) if i % 2 == 0]

    def test_extend(self):
        """
        None < == extend(iterable)
        1, 在原来列表的尾部增加元素
        2, 在原来的list上扩展, 改变了原来的list, 不会生成新的list
        3, L3 = L1 + L2   生成了新的list  L3
        4, iterable 可以是列表, 也可以是list, 等其他可以迭代的对象

        """
        _equal = self.assertEqual
        L = self.L.copy()
        L.extend([1, 3])
        _equal(len(L), 7)

        # 生成器
        g = (i for i in [11, 22, 33, 44])
        l1 = self.L.copy()
        l1.extend(g)
        assert l1 == [1, 2, 3, 4, 5, 11, 22, 33, 44]

        _equal(L.count(1), 2)
        _equal(L.count(3), 2)

        L = self.L.copy()
        L2 = L + [9, 99]
        self.assertEqual(L2[-1], 99)
        self.assertEqual(L2[-2], 9)

    def test_reverse(self):
        self.L.reverse()  # return None
        self.assertEqual(self.L, [5, 4, 3, 2, 1])

    def test_sort(self):
        """
        在原list上排序
        参数
            key = Optional
            reverse=False(默认值)  默认值-从小到大, 倒序-从大到小
        """
        L = self.L.copy()
        self.L.sort()
        self.assertEqual(L, self.L)

        self.L.sort(reverse=True)  # 倒序
        self.assertEqual(self.L, [5, 4, 3, 2, 1])

        L1 = ['b', 'a', 'c', 'e', 'd']
        l_zip = zip(L1, self.L)
        self.assertNotEqual(type(l_zip), list)

        l_zip = list(l_zip)
        l_zip.sort(key=lambda x: x[0])

        self.assertEqual(l_zip, [
            ('a', 4), ('b', 5), ('c', 3), ('d', 1), ('e', 2)
        ])

        # 复杂的排序
        numbers = [93, 86, 11, 68, 70]
        numbers.sort()
        self.assertEqual(numbers, [11, 68, 70, 86, 93])

        class Tool:
            def __init__(self, name, weight):
                self.name = name
                self.weight = weight

            def __repr__(self):
                return f'Tool({self.name!r}, {self.weight})'

        tools = [
            Tool('level', 3.5),
            Tool('hammer', 1.25),
            Tool('screwdriver', 0.5),
            Tool('chisel', 0.25),

        ]
        tools.sort(key=lambda x: x.name)
        self.assertEqual(tools[0].name, 'chisel')
        self.assertEqual(tools[1].name, 'hammer')
        self.assertEqual(tools[2].name, 'level')
        self.assertEqual(tools[3].name, 'screwdriver')

    def test_index(self):
        """
        index <== index(element)
            如果element不存在,则报错 ValueError

        """
        L = self.L.copy()
        try:
            inx = L.index(0)
        except ValueError:
            print('except')  # 执行
        else:
            print('else')  # 不执行
        finally:
            print('finally')  # 执行

        try:
            inx = L.index(1)
            self.assertEqual(inx, 0)
        except ValueError:
            print('except1')  # 不执行
        else:
            print('else1')  # 执行
        finally:
            print('finally1')  # 执行

    def test_insert(self):
        """
        None < = insert(pos, element)
        原来pos的位置的元素为ele
        则 insert之后, 其位置为pos+1, 新元素的位置为pos

        """
        L = self.L.copy()
        # 首部插入
        L.insert(0, 'j')  # None
        self.assertEqual(L[0], 'j')
        self.assertEqual(len(L), 6)

        l1, l2, l3, l4 = self.L.copy(), self.L.copy(), self.L.copy(), self.L.copy()
        # 末尾位置插入
        # 等效于L.append(..)
        pos = len(self.L)
        l2.insert(pos, 11)
        assert l2 == [1, 2, 3, 4, 5, 11]
        # 末尾的前一个位置
        l1.insert(pos-1, 11)
        assert l1 == [1, 2, 3, 4, 11, 5]
        # 超位置
        l3.insert(pos+4, 11)
        assert l3 == [1, 2, 3, 4, 5, 11]

        # -1 等价于  len(L)-1
        # 在末尾的前一个位置插入, 新插入的元素位置在倒数第二个
        l4.insert(-1, 11)
        assert l4 == [1, 2, 3, 4, 11, 5]
        pass

        # 如果要在一个元素的位置处插入数据,那么在他的索引处插入就可以了.
        l5 = self.L.copy()
        pos = l5.index(3)
        l5.insert(pos, 31)
        pos31 = l5.index(31)
        pos_ = l5.index(3)
        self.assertEqual(pos, pos31)
        # assert pos3 == pos31
        self.assertEqual(pos_, pos+1)

    def test_insert_and_index(self):
        L = self.L.copy()
        before = 2
        try:
            inx_befor = L.index(before)
            after = 9
            # 在索引的位置上插入新的值,新的值得索引值 == 原索引值
            L.insert(inx_befor, after)
            inx_after = L.index(after)
            self.assertEqual(inx_befor, inx_after)

            inx_before = L.index(before)
            self.assertEqual(inx_befor + 1, inx_before)
        except ValueError:
            pass

    def test_append(self):
        """
        None <== append(new)
            功能:在列表的尾部插入新的元素
            等效于: insert(len(L), new)
        """

        # insert  insert是在之前插入
        L = [1]
        L.insert(0, 2)  # return None
        self.assertEqual(L, [2, 1])

        pass

    def test_delete(self):
        """
        element <== pop(index)
            index 也就是元素的位置, index(索引)是从第0个位置开始的)
            返回值: 为该位置的元素

            pop() 等效于 pop(-1)
                也等效于  pop(len(L)-1)

        None <== remove(element)
        参数element是元素而不是索引
        如果element不存在,则报错 ValueError
        如果element有重复,则删除最前面的一个;

        del lit[index]
        删除 索引为index的元素
        也就是删除 第 index+1 个位置的元素

        clear()
        None < == (None)

        """

        # pop
        L = self.L.copy()
        result = L.pop()
        self.assertEqual(result, 5)
        result = L.pop(0)
        self.assertEqual(result, 1)

        l1 = self.L.copy()
        l2 = self.L.copy()
        l3 = self.L.copy()
        l1, l2, l3, l4 = self.L.copy(), self.L.copy(), self.L.copy(), self.L.copy()
        r1 = l1.pop(-1)
        r2 = l2.pop(len(l2)-1)
        r3 = l3.pop()
        # r4 = l4.pop(len(l4))   # IndexError: pop index out of range
        assert r1 == r2 == r3

        # remove
        l4 = self.L.copy()
        l5 = self.L.copy()
        l4.remove(2)
        assert l4 == [1, 3, 4, 5]

        l5.append(1)
        l5.remove(1)
        assert l5 == [2, 3, 4, 5, 1]

        try:
            l5.remove(6)
        except ValueError:
            print("ValueError...")

        # del
        L = self.L.copy()
        del L[0]
        self.assertEqual(L, [2, 3, 4, 5])
        #
        L = self.L.copy()
        del L[0], L[0]  # !!!
        self.assertEqual(L, [3, 4, 5])

        # clear
        L = self.L.copy()
        L.clear()
        self.assertEqual(L, [])

    def test_deepness_copy(self):
        L = [1, 2, 3, [5, 6], 7]
        L1 = L.copy()  # 支持深度copy
        self.assertEqual(L1[3], [5, 6])
        pass

    def test_section(self):
        # 切片的操作
        self.L.extend([6, 7])
        self.L.insert(0, 0)
        L = self.L.copy()
        self.assertEqual(L, [0, 1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(L[1:3], [1, 2])
        self.assertEqual(L[0:1], [0])
        self.assertEqual(L[:2], [0, 1])  # 不包括终点
        self.assertEqual(L[5:], [5, 6, 7])  # 包括起点
        self.assertEqual(L[5: len(L)], L[5:])
        self.assertEqual(L[:], L)
        # 负数切片, 负数总可以用 负数+列表长度 替换掉， 不管它在：的左边还是右边
        self.assertEqual(L[-3:], [5, 6, 7])
        self.assertEqual(L[5:-1], [5, 6])
        self.assertEqual(L[-3:-1], [5, 6])

        self.assertEqual(L[::], L)  # 复制全列表
        self.assertEqual(L[::1], L)  # 步长为1, 即为复制全列表
        self.assertEqual(L[::5], [0, 5])  # 0开始,步长为5
        self.assertEqual(L[::2], [0, 2, 4, 6])  # 0开始, 步长为2
        self.assertEqual(L[1::2], [1, 3, 5, 7])  # 1开始, 步长为2
        self.assertEqual(L[1:6:2], [1, 3, 5])  # 从1开始,不超过6, 步长为2

        self.assertEqual(L[::-1], [7, 6, 5, 4, 3, 2, 1, 0])  # 步长为-1, 即为倒序
        self.assertEqual(L[6:0:-2], [6, 4, 2])  # 6开始, 到0不包括0, 步长为-2

        # 身份
        l1 = self.L.copy()
        l2 = l1[:]
        l3 = l1[::]
        id1, id2, id3 = id(l1), id(l2), id(l3)
        self.assertNotEqual(id1, id2)
        self.assertNotEqual(id1, id3)

        # 切片元素的个数
        # L[a:b] : 切片元素的个数等于 b-a

        # 切片的应用之 切片出现在等号的左边, 可能会改变原列表的长度
        self.assertEqual(L, [0, 1, 2, 3, 4, 5, 6, 7])
        L1 = L.copy()
        # 元素减少
        # 2到7的元素用右边类别代替; 不包括7位置的数;
        L[2:7] = [99, 22, 14]
        self.assertEqual(L, [0, 1, 99, 22, 14, 7])

        # 元素增加
        L = L1
        L[2:3] = [22, 33]
        self.assertEqual(L, [0, 1, 22, 33, 3, 4, 5, 6, 7])

        # 如果出现在右边,等于是给这个列表做副本,虽然相同,但是身份不同
        b = L[:]
        self.assertNotEqual(id(b), id(L))

        # 用不在起止下标的切片放在赋值符号的左边,表示是用右边的那个列表的副本
        # 把左侧列表的全部内容替换掉(注意左边的列表依然保留原来的身份,系统不会分配新的列表)
        a = [1, 2, 3, 4, 5, 6]
        b = a
        a[:] = [101, 102, 103]
        self.assertTrue(a is b)
        self.assertEqual(a, [101, 102, 103])


if __name__ == '__main__':
    unittest.main()
