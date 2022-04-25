import unittest

import math


class MyTestCase(unittest.TestCase):
    def test_something(self):
        yu = divmod(10, 3)[1]  # chu发求余数
        self.assertEqual(yu, 1)

        pow = math.pow(2, 3)
        self.assertEqual(pow, 8)  # 2的3次方
        self.assertEqual(math.pow(4, 0.5), 2)  # 4的开方


if __name__ == '__main__':
    unittest.main()
