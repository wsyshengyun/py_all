import unittest


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.S = {1, 2, 3, 4, 5}

    def tearDown(self) -> None:
        pass

    def test_init(self):
        # 创建一个空集合,不能用{}形式
        s = set()
        # 只用一个参数, 可以是List, tuple 类型

        self.assertEqual({1, 2, 3}, {3, 2, 1})  # 没有顺序, 也是相等的

    def test_remove_repeat(self):
        """
        去掉重复的值
        :return:
        """
        s = {1, 2, 2, 3, 4}
        # 存储自动去重
        self.assertEqual(len(s), 4)
        self.assertEqual(s, {1, 2, 3, 4})
        # list做为参数
        l = [1, 2, 2]
        s = set(l)
        self.assertEqual(s, {1, 2})
        t = 1, 2, 2
        s = set(t)
        self.assertEqual(s, {1, 2})

        # 字符串也可以去重
        tsr = 'wsywsywsy'
        s = set(tsr)
        self.assertEqual(s, {'w', 's', 'y'})

    def test_operate(self):
        """操作"""
        s1 = {1, 2, 3, 4}
        s2 = {2, 3}
        s3 = {'a', 'b'}

        # - 操作
        self.assertEqual(s1 - s2, {1, 4})
        self.assertEqual(s2 - s1, set())  # 空值, 注意这里不能写为{}
        # self.assertEqual(s2 + s3, {'a', 'b', 2, 3})   !!!错误, 没有 + 操作

        # 交集 & == intersection
        set1 = {'a', 1, 2}
        set2 = {'b', 1, 2}
        set3 = set1.intersection(set2)
        self.assertEqual(set3, {1, 2})

        set3 = set1 & set2   # 同 intersection
        self.assertEqual(set3, {1, 2})

        # 交换顺序不影响什么
        set3 = set2.intersection(set1)
        self.assertEqual(set3, {1, 2})

        # 合并/联合  |
        set1 = {'a', 'b'}
        set2 = {1, 2}
        set3 = set1.union(set2)  # 返回一个新的set => set类型
        self.assertEqual(set3, {'a', 'b', 1, 2})
        self.assertNotEqual(set1, set3)

        set3 = set1 | set2  # 同union
        self.assertEqual(set3, {'a', 'b', 1, 2})

        # 不同的元素
        s1 = {'a', 1}
        s2 = {'b', 1, 2}
        s3 = s1.difference(s2)  # 属于s1的元素而不属于s2的元素
        self.assertEqual(s3, {'a'})

        s3 = s2.difference(s1)
        self.assertEqual(s3, {'b', 2})



    def test_CURD(self):
        """C 增 U改update  R 查找 D 删除
        集合建好以后,不能修改里面元素,只能新增或者移除
        """
        s1 = {1}
        s1.add(1)
        self.assertEqual(s1, {1})

        # 可以添加元组元素
        s1.add((1, 2, 3))
        self.assertEqual(s1, {1, (1, 2, 3)})

        # s1.add([4, 5])  不能添加列表元素
        # s1.add({'a':1})  不能添加字典元素

        s1 = {1}
        s1.add('hello')
        self.assertEqual(s1, {1, 'hello'})

        # update 列表
        s1 = {1}
        s1.update([1, 2, 3])
        self.assertEqual(s1, {1, 2, 3})

        # update 字典
        s1 = {1}
        s1.update({'a': 2})  # 字典只能添加键
        self.assertEqual(s1, {'a', 1})

        # update 元组
        s1 = {1}
        s1.update((2, 1, 4))
        self.assertEqual(s1, {1, 2, 4})

        # update string
        s1 = {1}
        s1.update('abc')
        self.assertEqual(s1, {1, 'a', 'b', 'c'})

        # update set
        s1 = {2, 3}
        s2 = {3, 4}
        s1.update(s2)
        self.assertEqual(s1, {2, 3, 4})

        pass

    def test_del(self):
        s1 = self.S.copy()
        s1.remove(1)  # => None
        self.assertEqual(s1, {2, 3, 4, 5})

        s1.discard(2)  # discard 丢弃
        # 如果删除的元素不存在,那么不会报错, 但是用remove会报错, 引发KeyError
        self.assertEqual(s1, {3, 4, 5})

    def test_pop(self):
        s = self.S.copy()
        # 随机删除一个元素, 好像从第一个开始, 返回结果为删除的元素
        result = s.pop()
        self.assertEqual(result, 1)
        result = s.pop()
        self.assertEqual(result, 2)

    def test_clear(self):
        self.S.clear()
        self.assertEqual(self.S, set())

        # 把集合释放掉
        del self.S

    def test_search(self):
        # 支持in操作
        self.assertEqual(1 in self.S, True)

    def test_9(self):
        pass


if __name__ == '__main__':
    unittest.main()
