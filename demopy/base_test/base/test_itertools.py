import itertools as it

import unittest


# from project.module.log import logger

class Myitertools(unittest.TestCase):

    def setUp(self):

        self.L = [1, 2, 3, 4, 5, 6]
        self.D = {'a': 1, 'b': 2, 'c': 3}
        # logger.info("self.L {}".format(self.L))
        pass

    def tearDown(self) -> None:

        pass

    def test_1count(self):

        nums = it.count()
        for i in nums:
            print("i is {}".format(i))
            if i > 6:
                break
        pass

        # 带部长的,和起始值的
        nums = it.count(2, 3)
        for i in nums:
            print("i(2,3) is :{}".format(i))
            if i > 30:
                break

    def test_2cycle(self):
        """
        cycle() 用于对 iterable 中的元素反复执行循环
        :return:
        """

        cycle_string = it.cycle('ABC')
        i = 0
        for tsr in cycle_string:
            print("tsr is : {}".format(tsr))
            i += 1

            if i == 10:
                break

    def test_3repeat(self):
        '''

        无限迭代器, repeat 用于反复生成一个object
        :return:
        '''
        iters = it.repeat('hello world', 3)
        for ele in iters:
            print("ele is {}".format(ele))

        iters = it.repeat([1, 2, 3, 4], 3)
        for ele in iters:
            print("ele is {}".format(ele))

    # -------------------------------------------------------------
    # 有限迭代器
    # -------------------------------------------------------------

    def test_4chain(self):
        '''
        可以连接多个迭代器
        :return:
        '''

        aiter = it.chain([1, 2, 3, 4], ['a', 'b', 'c'], ['+', '-'])
        # # for item in aiter:
        #   print("item is {}".format(item))

        self.assertEqual(aiter.__next__(), 1)
        self.assertEqual(aiter.__next__(), 2)
        self.assertEqual(aiter.__next__(), 3)
        self.assertEqual(aiter.__next__(), 4)
        b, *_, c, d = aiter
        self.assertEqual(b, 'a')
        self.assertEqual(c, '+')
        self.assertEqual(d, '-')

        aiter = it.chain.from_iterable('ABCD')
        self.assertEqual(next(aiter), 'A')
        self.assertEqual(next(aiter), 'B')
        self.assertEqual(next(aiter), 'C')
        self.assertEqual(next(aiter), 'D')

    def test_5compress(self):
        '''
        当;selector数列的元素为真时,保留data响应位置的元素.
        :return:
        '''

        data = 'ABCD_EFG'
        selector = [1, 1, 1, 1, 0, 0, 0, 1]
        aiter = it.compress(data, selectors=selector)
        self.assertEqual(next(aiter), 'A')
        self.assertEqual(next(aiter), 'B')
        self.assertEqual(next(aiter), 'C')
        self.assertEqual(next(aiter), 'D')
        self.assertEqual(next(aiter), 'G')

    def test_6dropwhile(self):

        aiter = it.dropwhile(lambda x: x < 5, [1, 3, 6, 9, 10, 2])
        self.assertEqual(next(aiter), 6)
        self.assertEqual(next(aiter), 9)
        self.assertEqual(next(aiter), 10)
        self.assertEqual(next(aiter), 2)
        pass

    def test_7groupby(self):

        aiter = it.groupby('aaabbbcddddddeff')

        print("{}".format(next(aiter)))
        for key, val in aiter:
            print("keyis {}, val is {}".format(key, list(val)))
        pass

    def test_8dict_iter(self8):
        D = {'a': 1, 'b': 2}
        aiter = iter(D)
        # logger.info("aiter{}".format(next(aiter)))

        print("{}".format(next(aiter)))
        print("{}".format(next(aiter)))

        # for key, val in aiter:
        # logger.info("{} - {}".format(key, val))  # 报错

    def test_9ifilter(self):
        '''
        !!! itertools has no attribute 'ifilter
        :return:
        '''
        # itera = it.ifilter(lambda x: x<3, self.L)
        # L = list(itera)
        # logger.info("L is {}".format(L))

        pass

    def test_90ifilterfalse(self):
        pass

    def test_91islice(self):
        '''
        注意start和end指的是 位置position
        从 start开始 包含 start位置
        到end结束,但也不包含end位置
        :return:
        '''
        self.L.extend([6, 7, 8, 9, 10, 1, 12])

        print("self.L: {}".format(self.L))
        itera = it.islice(self.L, 2, 13, 1)
        L = list(itera)
        print("L is {}".format(L))

        L = list(it.islice(self.L, 5))  # 5指的是end位置
        print("L is {}".format(L))

        # 配合count
        L = list(it.islice(it.count(), 0, 8, 2))
        print("count L is {}".format(L))
        pass

    def test_92imap(self):
        '''
        not function
        :return:
        '''

        pass

    def test_93tee(self):
        '''
        itertools.tee
        参数为一个迭代器, 可以生成一个含有3个同样迭代器元素的元组.
        例如: itertools.tee(iter, 3) => (iter, iter, iter)
        :return:
        '''

        itera = it.tee(self.L, 3)

        print("itera type is {}".format(type(itera)))
        L = list(itera)
        for ele in L:
            print("ele is {}".format(list(ele)))
            pass
        # logger.info("L is {}".format(L))

        pass

    def test_94_takewhile(self):
        L = [1, 2, 3, 6, 4, 7]
        aiter = it.takewhile(lambda x: x < 5, L)
        L = list(aiter)

        print("takewhile L is {}".format(L))

    def test_95_izip(self):
        '''
        not function
        :return:
        '''
        pass

    def test_96_izip_longest(self):
        '''
        it.combinations(L, n), n:必须是一个int类型的
        L 必须是一个序列, 不能是一个迭代器
        :return:
        '''
        L = [2, 2, 4]
        L = (i for i in L)
        L = list(L)
        result = it.combinations(L, 2)
        for i, j in result:
            if i == j:
                break
        else:
            self.assertRaises("nihao")

        result = it.combinations(L, 2)
        print(list(result))
        pass
