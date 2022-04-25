import unittest

from lxml import etree


class MyXpathTest(unittest.TestCase):

    def setUp(self):
        self.tstr = '<bookstore>' \
                    '<book>' \
                    '<title lang="bng" src="https://www.baidu.com">Harry Potter</title>' \
                    '<price>29.99</price>' \
                    '</book>' \
                    '<book>' \
                    '<title class="t1" lang="ang">Learning XML</title>' \
                    '<price>39.95</price>' \
                    '</book>' \
                    '<book>' \
                    '<title lang="cng">西游记</title>' \
                    '<price>69.95</price>' \
                    '</book>' \
                    '<book>' \
                    '<title lang="dng" src="https://www.jd.com">水浒传</title>' \
                    '<price>29.95</price>' \
                    '</book>' \
                    '<book>' \
                    '<title class="t1" lang="dng" src="https://www.jd.com">三国演义</title>' \
                    '<price>29.95</price>' \
                    '</book>' \
                    '</bookstore>'
        self.html = etree.HTML(self.tstr)
        # logger.info("html is {}".format(html))
        content = etree.tostring(self.html, encoding='utf8')
        # logger.info("content.decode() = {}".format(content.decode()))
        """ 
        tostring() 返回的是二进制内容; 
        如果要查看字符串,需要先解码
        如果要查看汉字,需要先编码,再解码
        """

        pass

    def tearDown(self) -> None:
        pass

    def test_xpath_1_signal(self):
        title = self.html.xpath('//title/text() | //price/text()')
        self.assertEqual(type(title), list)
        self.assertIn('Harry Potter', title)
        self.assertIn('29.99', title)
        self.assertIn('39.95', title)
        self.assertIn('Learning XML', title)

        pass

    def test_path(self):
        text = self.html.xpath('//title[@lang="cng"]//text()')
        self.assertEqual(text, ["西游记"])

        text = self.html.xpath('//book[1]/title/text()')
        # 注意此处的[1] 不能再title后面,这样是选出了所有的text;
        # 因为如果//book 就是选择所有的book,如何title[1] ,那就是选择所有book的title
        self.assertEqual(text, ["Harry Potter"])

        # 获取最后一个book的title的内容 
        text = self.html.xpath('//book[last()]/title/text()')
        self.assertEqual(text, ["三国演义"])

        #  position() 位置
        text = self.html.xpath('//book[position()>3]/title/text()')
        self.assertEqual(text, ["水浒传", "三国演义"])

        # position() 3<position <5   and 
        text = self.html.xpath('//book[position()>3 and position()<5]/title/text()')
        self.assertEqual(text, ["水浒传"])

        #  position()   or 
        text = self.html.xpath('//book[position()=2 or position()=5]/title/text()')
        self.assertEqual(text, ["Learning XML", "三国演义"])

        # /title[@src] 
        text = self.html.xpath('//book/title[@src]/text()')
        self.assertEqual(text, ["Harry Potter", "水浒传", "三国演义"])

        # text = self.html.xpath('')
        # text = self.html.xpath('')
        # self.assertEqual(text, [])
        # self.assertEqual(text, [])

        pass
