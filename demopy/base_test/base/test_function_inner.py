import unittest


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_1(self):
        # 进制装换
        a = 10
        # print(bin(a))
        self.assertEqual(bin(a), "0b1010")
        self.assertEqual(oct(a), "0o12")
        self.assertEqual(hex(a), '0xa')

        # chr
        self.assertEqual(chr(97), 'a')

    def test_2(self):
        # 字符串常用操作
        # replace
        stra = 'I love python3 very much'
        str_reped = stra.replace('love', 'like')
        self.assertEqual(str_reped, 'I like python3 very much')

        # join
        a = '; '
        b = '123'
        c = a.join(b)  # 把b看成了一个列表了
        self.assertEqual(c, "1; 2; 3")

        # split
        strc = 'the way to mad'
        lit = strc.split(' ')
        self.assertEqual(lit[0], 'the')

        # format
        # strip
        self.assertEqual('\t\n python'.strip(), 'python')
        self.assertEqual(' python'.lstrip(), 'python')
        self.assertEqual('python '.rstrip(), 'python')
        self.assertEqual('aabbcc'.strip('ac'), 'bb')

    def test_3(self):
        # map
        L = [1, 2, 3]
        mapobj = map(lambda x: x > 2, L)
        self.assertEqual(type(mapobj).__name__, 'map')
        self.assertEqual(list(mapobj), [False, False, True])

        self.assertEqual(L, [1, 2, 3])

        # reduce
        from functools import reduce
        value = reduce(lambda x, y: x * y, L)
        self.assertEqual(value, 6)

        # filter
        result = filter(lambda x: x > 2, L)
        self.assertEqual(list(result), [3])
        self.assertEqual(type(result).__name__, 'filter')

        # zip
        l1 = [1, 2, 3]
        l2 = 'a', 'b', 'c'
        ll = zip(l1, l2)
        self.assertEqual(type(ll).__name__, 'zip')
        self.assertEqual(list(ll), [(1, 'a'), (2, 'b'), (3, 'c')])

        # zip2
        l1 = [1, 2, 3, 4, 5]
        l2 = 'a', 'b'
        ll = zip(l1, l2)
        self.assertEqual(list(ll), [(1, 'a'), (2, 'b')])

        ll = zip(l2, l1)
        self.assertEqual(list(ll), [('a', 1), ('b', 2)])

        # enumerate
        for i, k in enumerate(range(2, 7), start=0):
            # print(i, k)
            self.assertEqual(i + 2, k)

        self.assertEqual(list(enumerate(range(4))),
                         [(0, 0), (1, 1), (2, 2), (3, 3)])

    def test_4(self):
        pass

    def test_5(self):
        pass

    def test_6(self):
        pass

    def test_7(self):
        pass

    def test_8(self):
        pass

    def test_9(self):
        pass


if __name__ == '__main__':
    unittest.main()
