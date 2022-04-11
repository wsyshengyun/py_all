import unittest


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.D = {'a': 1, 'b': 2, 'c': 3}
        pass

    def test_something(self):
        D = {}
        self.assertEqual(D, {})

        D = dict()
        self.assertEqual(D, {})

        tup = [('a', 1), ('b', 2), ('c', 3)]
        D = dict(tup)
        self.assertEqual(self.D, D)
        # self.assertEqual(id(self.D), id(D))  False

        D = dict.fromkeys([1, 2, 3], "a")  # 1, 2, 3是键  'a'是值
        self.assertEqual(D, {1: 'a', 2: 'a', 3: 'a'})

        D = dict(a=1, b=2, c=3)
        self.assertEqual(D, self.D)

        D = {}
        D['a'] = 1
        D['b'] = 2
        D['c'] = 3
        self.assertEqual(D, self.D)

        D = {}
        D.setdefault('four')
        self.assertEqual(D, {'four': None})

        D = {}
        D.setdefault('d', 9)
        self.assertEqual(D, {'d': 9})
        D = self.D
        result = D.setdefault('a', 5)
        self.assertEqual(result, 1, msg='nihao')  # 当错误的时候才打印Msg
        self.assertEqual(D, self.D)
        # 当'd' 存在的时候, 字典D不会改变, setdefault返回原来'd'的值;
        # 当'd' 不存在的时候, 字典D新加入一个元素, 'd':9

        D = self.D
        result = D.setdefault('d', 5)
        self.assertEqual(result, 5)
        self.assertEqual(D, {'a': 1, 'b': 2, 'c': 3, 'd': 5})

    def test_dict_function(self):
        D = self.D
        result = D.update(d=5)
        self.assertEqual(D, {'a': 1, 'b': 2, 'c': 3, 'd': 5})
        self.assertEqual(result, None)

        result = D.update({'d':5})
        self.assertEqual(D, {'a': 1, 'b': 2, 'c': 3, 'd': 5})
        self.assertEqual(result, None)

    def test_dict_function_remove(self):
        result = self.D.pop('a')
        self.assertEqual(len(self.D), 2)
        self.assertEqual(result, 1)

    def test_clear(self):
        D = self.D
        self.D.clear()
        self.assertEqual(self.D, {})
        self.assertEqual(D, {})

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

    def test_popitem(self):
        D = self.D
        new = D.copy()
        self.assertEqual(D, new)

        D.popitem()
        self.assertEqual(D, {'a': 1, 'b': 2})

    def test_some(self):
        self.assertEqual([(), ()], [(), ()])








if __name__ == '__main__':
    unittest.main()
