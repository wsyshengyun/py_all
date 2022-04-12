import unittest


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.D = {'a': 1, 'b': 2, 'c': 3}
        pass

    def test_something(self):
        # {}
        D = {}
        self.assertEqual(D, {})

        D = dict()
        self.assertEqual(D, {})

        # zip
        tup = [('a', 1), ('b', 2), ('c', 3)]
        D = dict(tup)
        self.assertEqual(self.D, D)

        l1 = ['a', 'b', 'c']
        l2 = [1, 2, 3]
        l = zip(l1, l2)
        self.assertNotEqual(type(l), list)
        D = dict(l)
        self.assertEqual(D, self.D)

        # fromkeys(keys.., 'one_value')
        D = dict.fromkeys([1, 2, 3], "a")  # 1, 2, 3是键  'a'是值
        self.assertEqual(D, {1: 'a', 2: 'a', 3: 'a'})

        # dict( = )
        D = dict(a=1, b=2, c=3)
        self.assertEqual(D, self.D)

        # {}
        D = {}
        D['a'] = 1
        D['b'] = 2
        D['c'] = 3
        self.assertEqual(D, self.D)

        # 字典合并来创建新的字典
        D1 = {'a':1, 'b':2}
        D2 = {'b':3, 'd':4}
        D = {**D1, **D2}  # 解包
        self.assertEqual(D, {'a':1, 'b':3, 'd':4})  # !!! 'b':2被覆盖
        D = {**D2, **D1}
        self.assertEqual(D, {'a':1, 'b':2, 'd':4})  # 后面的覆盖前面的

    def test_setdefault(self):
        """
        D.setdefault(key, val): 如果key in D, 那么val不会覆盖D里面key的值
        如果key not in D, 那么key:val键值对会加入D

        D[key] = val
        如果之前key in D, 那么val会覆盖原来的值
        如果key not in D, 那么key:val键值对会加入D

        :return:
        """

        D = {}
        D.setdefault('four')  # <==> setdefault('four', None)
        self.assertEqual(D, {'four': None})

        #
        D = self.D.copy()
        result_if_exist_key = D.setdefault('a', 11)
        self.assertEqual(D, {'a':1, 'b':2, 'c':3})
        self.assertEqual(result_if_exist_key, 1)

        result_if_not_exist_key = D.setdefault('d', 4)
        self.assertEqual(result_if_not_exist_key, 4)

        # 与setdefault相反,存在键值,直接覆盖
        D = self.D.copy()
        D['a'] = 2
        self.assertEqual(D, {'a':2, 'b':2, 'c':3})

    def test_dict_function(self):
        # k=v
        D = self.D.copy()
        result = D.update(d=5)  # result -> None
        self.assertEqual(D, {'a': 1, 'b': 2, 'c': 3, 'd': 5})

        # {..}
        D = self.D.copy()
        result = D.update({'d': 5})
        self.assertEqual(D, {'a': 1, 'b': 2, 'c': 3, 'd': 5})

        # **D1
        D = self.D.copy()
        D1 = {'d': 5}
        D.update(**D1)
        self.assertEqual(D, {'a':1, 'b':2, 'c':3, 'd':5})

        # 遇到相同的键,覆盖掉
        D = self.D.copy()
        D.update({'c': 33})
        self.assertEqual(D, {'a': 1, 'b': 2, 'c': 33})

    def test_dict_function_remove(self):
        result = self.D.pop('a')
        self.assertEqual(len(self.D), 2)
        self.assertEqual(result, 1)

    def test_clear(self):
        D = self.D
        self.D.clear()
        self.assertEqual(self.D, {})
        self.assertEqual(D, {})

    def test_popitem(self):
        """
        pipitem
        不带参数
        后返回键和值得元祖
        :return:
        """
        D = self.D.copy()

        result = D.popitem()
        self.assertEqual(D, {'a': 1, 'b': 2})
        self.assertEqual(result, ('c', 3))

    def test_items_values(self):
        D = self.D
        items = D.items()
        keys = D.keys()
        values = D.values()
        self.assertEqual(list(values), [1, 2, 3])
        self.assertEqual(list(keys), ['a', 'b', 'c'])

        self.assertEqual(type(keys).__name__, 'dict_keys')
        self.assertEqual(type(values).__name__,
                         'dict_values')
        self.assertEqual(type(items).__name__,
                         'dict_items')
        pass

    def test_some(self):
        self.assertEqual([(), ()], [(), ()])
        D = {'a':1, 'a':2}
        self.assertEqual(D, {'a': 2})

    def test_get(self):
        D = self.D.copy()
        r_a = D.get('a', 'default')
        r_d = D.get('d', 'default')
        self.assertEqual(r_a, 1)
        self.assertEqual(r_d, 'default')

    def test_sort(self):
        D = {'a': 9, 'd': 1, 'c': 3, 'b': 11}
        L = list(D.items())
        L.sort(key=lambda x: x[1])
        self.assertEqual(L[0], ('d', 1))
        self.assertEqual(L[-1], ('b', 11))




if __name__ == '__main__':
    unittest.main()
