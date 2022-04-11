import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.L = [1, 2, 3, 4, 5]

    def test_something(self):
        _equal = self.assertEqual

        L = []
        L1 = list()
        _equal(L, L1)

        L = [1, 2, 3, 4, 5]
        _equal(L, self.L)

        L.append(6)
        _equal(L, [1, 2, 3, 4, 5, 6])

    def test_pop(self):
        _equal = self.assertEqual
        L = self.L
        L.pop(-1)  # index
        _equal(L, [1, 2, 3, 4])

        L.pop(1)
        _equal(L, [1, 3, 4])

        L.pop()  # 末尾
        _equal(L, [1, 3])

    def test_extend(self):
        _equal = self.assertEqual
        L = self.L
        L.extend([1, 3])
        _equal(len(L), 7)

        _equal(L.count(1), 2)
        _equal(L.count(3), 2)

    def test_clear(self):
        self.L.clear()
        self.assertEqual(self.L, [])

    def test_remove(self):
        self.L.remove(1)  # not return value
        self.assertEqual(self.L, [2, 3, 4, 5])

    def test_reverse(self):
        self.L.reverse()  # return None
        self.assertEqual(self.L, [5, 4, 3, 2, 1])

    def test_sort(self):
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

    def test_insert_and_copy(self):
        L = self.L.copy()
        self.assertEqual(len(self.L), 5)
        self.L.insert(0, 'j')  # None
        self.assertEqual(self.L[0], 'j')
        self.assertEqual(len(self.L), 6)

        flen = lambda : len(self.L)
        self.assertNotEqual(L, self.L)

        L1 = L.copy()
        L.insert(flen(), 8)  # 末尾+1 超范围了
        L1.insert(flen()-1, 8)  # 末尾
        self.assertEqual(L, L1)   # ==

    def test_index(self):
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

    def test_insert_and_index(self):
        L = self.L.copy()
        self.assertEqual(L, [1, 2, 3, 4, 5])
        find_ele = 2
        try:
            inx = L.index(find_ele)
            b = 9
            L.insert(inx, b)
            inx_b = L.index(b)
            self.assertEqual(inx, inx_b)

            inx_find_ele = L.index(find_ele)
            self.assertEqual(inx+1, inx_find_ele)
        except ValueError:
            pass







if __name__ == '__main__':
    unittest.main()
