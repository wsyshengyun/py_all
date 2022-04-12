import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.L = [1, 2, 3, 4, 5]

    def test_create_list(self):
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

    def test_extend(self):
        _equal = self.assertEqual
        L = self.L.copy()
        L.extend([1, 3])
        _equal(len(L), 7)

        _equal(L.count(1), 2)
        _equal(L.count(3), 2)

        L = self.L.copy()
        L2 = L + [9, 99]
        self.assertEqual(L2[-1], 99)
        self.assertEqual(L2[-2], 9)

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
        self.assertEqual(len(L), 5)
        L.insert(0, 'j')  # None
        self.assertEqual(L[0], 'j')
        self.assertEqual(len(L), 6)

        L1 = L.copy()
        L.insert(len(L), 8)  # 末尾位置插入
        L1.insert(len(L1) - 1, 8)  # 末尾得前一个位置
        self.assertNotEqual(L, L1)  # ==

    #     如果要在一个元素的位置处插入数据,那么在他的索引处插入就可以了.

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
            L.insert(inx, b)  # 在索引的位置上插入新的值,新的值得索引值 == 原索引值
            inx_b = L.index(b)
            self.assertEqual(inx, inx_b)

            inx_find_ele = L.index(find_ele)
            self.assertEqual(inx + 1, inx_find_ele)
        except ValueError:
            pass

    def test_add(self):
        # append
        L = []
        L.append(1)  # return None
        self.assertEqual(L, [1])

        # insert  insert是在之前插入
        L = [1]
        L.insert(0, 2)  # return None
        self.assertEqual(L, [2, 1])

        pass

    def test_delete(self):
        # pop
        L = self.L.copy()
        result = L.pop()
        self.assertEqual(result, 5)
        result = L.pop(0)
        self.assertEqual(result, 1)

        # remove
        L = self.L.copy()
        L.insert(2, 1)  # 在索引之前插入
        self.assertEqual(L, [1, 2, 1, 3, 4, 5])
        L.remove(1)  # 删除第一出现的1
        self.assertEqual(L, [2, 1, 3, 4, 5])

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


if __name__ == '__main__':
    unittest.main()
