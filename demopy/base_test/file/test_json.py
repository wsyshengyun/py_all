import json
import unittest

""" 
关于编码和解码
编码就是把本平台的对象编码为不认识的,或者方便传输的字符
解码就是把不方便认识的字符,转换为可以认识的,本平台的字符.

比如编码 encoding('utf-8') 把一个字符串编码为utf8后世一堆十六进制的字符串.
然后解码就是decoding('utf-8')  把十六进制的字符串转换为可以识别的字母或者汉字.

"""


class MyJsonTest(unittest.TestCase):

    def setUp(self):
        self.path = 'project/log/tt.json'

        pass

    def tearDown(self):
        pass

    def test_dumps(self):
        data = json.dumps([])
        self.assertEqual(data, '[]')

        d2 = json.dumps(2)
        self.assertEqual(d2, '2')

        d3 = json.dumps(3)
        self.assertEqual(d3, '3')

        D = {'name': 'Tom', 'age': 23}
        d4 = json.dumps(D)
        self.assertEqual(d4, '{"name": "Tom", "age": 23}')
        self.assertEqual(d4, str(D).replace('\'', '\"'))

        pass

    def test_dump(self):
        D = {'name': 'Tom', 'age': 23}
        with open(self.path, 'w', encoding='utf-8') as f:
            f.write(json.dumps(D, indent=4))
        pass

    def test_loads(self):
        """ 将字符串还原称为dict """
        # D = "{'name':'Toms', 'age':23}" 
        D = '{"name":"Toms", "age":23}'  # !!! 上面的不可以转换为dict对象 
        d1 = json.loads(D)
        self.assertEqual(type(d1), dict)
        self.assertEqual(d1.get('name'), 'Toms')
        pass

    def test_load(self):
        """ 注意区分loads和load
        loads 加载的是字符串类型; 
        load加载的是文件对象; 
        """
        with open(self.path, 'r', encoding='utf-8') as f:
            d1 = f.read()
            d2 = json.loads(d1)
            self.assertEqual(type(d2), dict)
            self.assertEqual(d2.get('name'), 'Tom')

            f.seek(0)
            d3 = json.load(f)
            self.assertEqual(type(d3), dict)
            self.assertEqual(d3.get('name'), 'Tom')
        pass

    def test_manyline_load(self):
        path = 'project/log/manyline.json'
        with open(path, 'r', encoding='utf-8') as f:
            # joinstr = ''.join([line.strip() for line in f])
            joinstr = ''.join([line for line in f])
            new = '{"dict":[' + joinstr + '[}'
            d1 = json.dumps(new)
            print(d1)

        pass

    def test_convert_file(self):
        # TODO SS 如何将一个txt文件转换为utf8格式??
        path = 'project/log/manyline.json'
        pass
