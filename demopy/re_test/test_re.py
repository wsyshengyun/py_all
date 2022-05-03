import unittest
import re
from typing import Union

"""
r的作用
表示原生字符串

\w      匹配字母数字及下划线
\W      匹配f非字母数字下划线
\s      匹配任意空白字符，等价于[\t\n\r\f]
\S      匹配任意非空字符
\d      匹配任意数字
\D      匹配任意非数字
\A      匹配字符串开始
\Z      匹配字符串结束，如果存在换行，只匹配换行前的结束字符串
\z      匹配字符串结束
\G      匹配最后匹配完成的位置
\n      匹配一个换行符
\t      匹配一个制表符
^       匹配字符串的开头
$       匹配字符串的末尾
.       匹配任意字符，除了换行符，re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符
[....]  用来表示一组字符，单独列出：[amk]匹配a,m或k
[^...]  不在[]中的字符：[^abc]匹配除了a,b,c之外的字符
*       匹配0个或多个的表达式
+       匹配1个或者多个的表达式
?       匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
{n}     精确匹配n前面的表示
{m,m}   匹配n到m次由前面的正则表达式定义片段，贪婪模式
a|b     匹配a或者b
()      匹配括号内的表达式，也表示一个组
re.I(re.IGNORECASE): 忽略大小写（括号内是完整写法）
re.M(re.MULTILINE): 多行模式，改变'^'和'$'的行为
re.S(re.DOTALL): 点任意匹配模式，改变'.'的行为
"""


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.tsr1 = "hello python"
        self.tsr2 = '7Hello python'
        self.tsr_china = "人间大炮1级准备"
        self.tsr_abc_china = "人间china 大炮1级准备"
        self.tsr_space = 'hello python  table'

        pass

    @staticmethod
    def match(pattern, tsr):
        result = re.match(pattern, tsr)
        if result:
            return result.group()

    def tearDown(self) -> None:
        pass

    def test_signle(self):
        """
        \D 匹配非数字

        """
        result = self.match('\D*', self.tsr_china)
        self.assertEqual(result, "人间大炮")

        result1 = self.match(r'\w+', self.tsr_china)
        self.assertEqual(result, "人间大炮")

        # 把整个字符串匹配完了
        _ = self.match('\D*.\D*', self.tsr_china)
        # result_if_none is "" 字符串
        result_if_none = self.match('', self.tsr_china)

        #
        # \d
        #
        assert self.match('\d', '1')
        assert self.match('\d', '0')
        assert self.match('\d+', '222')
        assert self.match('\d+', '000')
        # assert self.match('\d', '一')
        # assert self.match('\d', 'a')
        # assert self.match('\d', 'b')


        #
        #  \S 匹配非空白
        #
        _1 = self.match('\S*', self.tsr_abc_china)
        assert self.match('\S', 'a')
        assert self.match('\S', 'z')
        assert self.match('\S', '中国')
        # assert self.match('\S', '\n')  报错
        # assert self.match('\S', '')
        # assert self.match('\S', ' ')

        #
        # \s  匹配空白字符
        #

        assert self.match('\s', '\t')
        # assert self.match('\s', '\s')
        assert self.match('\s', '\n')
        assert self.match('\s', '\r')
        assert self.match('\s', ' ')
        assert self.match('\s', '\f')  # 换页
        assert self.match('\s', '\v')
        # assert self.match('\s', '')

        #
        # \w [a-z A-Z 0-9 - ] 单词类字符
        #
        assert self.match('\w', '_')
        assert self.match('\w', 'a')
        assert self.match('\w', 'z')
        assert self.match('\w', 'A')
        assert self.match('\w', 'Z')
        assert self.match('\w', '0')
        assert self.match('\w', '9')
        # assert self.match('\w', '-')
        # assert self.match('\w', '@')
        assert self.match('\w', '中')
        china = "中"
        utf = china.encode('utf8')
        # TypeError: cannot use a string pattern on a bytes-like object
        # assert self.match('\w', utf)

        #
        # \W  非\w
        #
        assert self.match('\W', '+')
        assert self.match('\W', '-')
        assert self.match('\W', '\n')
        assert self.match('\W', '\t')
        assert self.match('\W', '\b')
        assert self.match('\W', '\h')
        assert self.match('\W', '\A')
        assert self.match('\W', '\B')
        assert self.match('\W', '$')
        assert self.match('\W', '#')
        assert self.match('\W', '@')
        assert self.match('\W', '!')
        assert self.match('\W', '(')
        assert self.match('\W', ')')
        assert self.match('\W', '{')

        # assert 1
        # assert 'a'
        # assert [1]
        # assert set()  报错
        # assert {}  报错
        # assert []  报错
        # assert 0  报错
        # assert False  报错
        # assert None  报错
        # assert ''  报错

        pass

    def test_many(self):
        """
        匹配多个字符
        []
        [^-] 除了-之外的
        {m}
        {m, n}
        {,n} <==> {1, n}
        {m,} <==> 最少匹配m次

        """
        # assert self.match('[A-Z][a-z]', 'M')
        assert self.match('[A-Z][a-z]', 'Mm')
        assert self.match('[A-Z][a-z]', 'Mmc')
        assert self.match('[A-Z]', 'M')
        assert self.match('[a-z]', 'm')
        assert self.match('[a-zA-Z]', 'M')
        # assert self.match('[a-zA-Z]', '0')
        assert self.match('[a-zA-Z0-9]', '8')
        assert self.match('[a-zA-Z-]', '-')
        assert self.match('[a-zA-Z-中]', '中')
        # assert self.match('[a-Z]', 'b')

        assert self.match('[^-]', 'b')
        assert self.match('[^-]', '0')
        assert self.match('[^-]', '_')
        assert self.match('[^-]', ' ')
        # assert self.match('[^-]', '-')
        assert self.match('[^a]', 'b')
        assert self.match('[^a]', 'A')
        # assert self.match('[^a]', 'a')

        assert self.match('[A-Z]{6}', 'ABCDEF')
        assert self.match('[A-Z]{6}', 'ABCDEFG')
        assert self.match('[A-Z]{2,4}', 'DEFGG')
        assert self.match('[A-Z]{2,4}', 'DEFG')
        assert self.match('[A-Z]{2,4}', 'FG')
        # assert self.match('[A-Z]{2,4}', 'G')

        assert self.match('[A-Z]{2,}', 'FG')
        # assert self.match('[A-Z]{2,}', 'G')
        # assert self.match('[A-Z]{,2}', '')
        assert self.match('[A-Z]{,2}', 'A')
        assert self.match('[A-Z]{,2}$', 'AB')
        # assert self.match('[A-Z]{,2}$', 'ABC')

        pass

    def test_head_tail(self):
        """
        匹配开始和结尾
        ^ 开始
        $ 结尾

        """
        assert self.match('^a', 'abc')
        # assert self.match('^a', 'bca')
        # assert self.match('c$', 'abc')
        assert self.match('^abc$', 'abc')
        # assert self.match('^ac$', 'abc')
        assert self.match('abc$', 'abc')
        pass

    def test_group(self):
        """
        匹配分组
        | 匹配左右任意一个表达式
        (ab) 将括号里面的字符作为一个分组
        \num 引用分组num匹配到的字符串
        (?P) 分组起别名
        {?P=name) 引用别名为name的分组匹配到的字符串

        """
        #
        # |
        #
        assert self.match('[1-9]?\d|100', '798')   # 79
        result1 = self.match(r'[1-9]??\d|100', '789')
        assert result1 == '7'
        assert self.match('[1-9]?\d|100', '058')  # 0
        assert self.match('[1-9]?\d|\w\d\d', 'a08')  # a08
        #
        # ()
        #
        ret = re.match('([^-]*)-(\d+)', '010-12345678')
        r1 = ret.group()
        r2 = ret.group(1)
        r3 = ret.group(2)
        # r4 = ret.group(3)  报错
        #
        # \
        #
        # r'' r要加上 不然要报错, 因为里面有\w
        ret = re.match(r'<([a-zA-Z]*)>\w*</\1>', '<html>hh</html>')
        r4 = ret.group()
        r5 = ret.group(1)

        # 分组起别名
        # 初始化名称 => (?P<name>xxx) xxx为正则表达式
        # 引用别名 => (?P=name)
        #

        htmls = "<html><h1>www.baidu.com</h1></html>"
        pattern = r'<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>'

        # pattern = r'<(\w*?P<name1>)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>'
        # 此处错误 上面 > \w* 要放在后面, ?P放在前面

        # ret : <Match>
        # ret.groupdict() return <dict>
        # 注意结果只有group1 和 group2

        # Match.lastgroup : <str> 'name2'
        # Match.lastindex : <int> 2
        # Match.pos : <int> 0
        # Match.endpos : <int> 35  == len(htmls)
        # Match.re : <Pattern>
        # Match.regs : <tuple> ((0, 35), (1, 5), (7, 9))
        # Match.string : <str> htmls
        ret = re.match(pattern, htmls)
        if ret:
            r6 = ret.group()
            r7 = ret.group(1)
            r8 = ret.group(2)
            # r9 = ret.group(3)
            # r10 = ret.group(4)
            r11 = ret.groupdict()
        pass

    def test_match(self):
        """
        正则表达式高级用法
        匹配对象 或 None< == re.match(
            pattern,
            string,
            flags = 0  标志位 用于控制正则表达式的匹配方式
                        大小写 | 多行匹配
        )
        1, match 在起始位置匹配, 否则返回None
        2, 如果匹配到了 返回 Match对象
        3, 如果没有匹配到 返回None


        Match对象方法:
            group(num=0) => 匹配的整个表达式的字符串
            num: 0 匹配的全部字符串
                1, 第一组 ()  字符串
                2, 第二组 () 字符串
                3, ...
            groups() => 返回一个所有小组字符串的元祖

        Match对象属性:
            endpos  结束匹配的位置 一般等于字符串的长度, 因为匹配完了, 如果没有完全匹配完字符串, 那么就不是这个值了
            lastgroup
            lastindex
            pos  开始匹配的位置 从0开始
            re <Pattern>
            regs <tuple>
            string <str>

        """
        reslut1 = re.match(r'b', 'abc')
        reslut2 = re.match(r'a', 'abc')
        reslut3 = re.match(r'ac', 'abc')
        pass

    def test_search(self):
        """
        匹配对象或者None <== search(pattern, string, flags=0)
        search 扫描整个字符串,并返回第一个成功的匹配.

        """
        line = 'Cats are smarter than dogs'
        pattern = r'(.*?) are (.*?) .*'
        pattern = r'(.*) are (.*) .*'
        search_obj = re.search(pattern, line, re.M | re.I)
        if search_obj:
            v1 = search_obj.group()
            v2 = search_obj.group(1)
            v3 = search_obj.group(2)
        else:
            print('Nothing found!')

        # 
        # re.I 忽略大小写
        # 
        assert re.search(r'a', 'a', re.I)
        assert re.search(r'a', 'A', re.I)
        assert re.search(r'a', 'a')
        # assert re.search(r'a', 'A')

        #
        # re.M
        #
        tsr = """abc
         999"""
        tsr = 'abc\n999'
        assert re.search(r'\d', tsr, re.M)
        assert re.search(r'\d', tsr)
        pass

    def test_findall(self):
        """
        [...] 或者 []< = findall(string[, pos[, endpos]])
        与以上的区别: findall是匹配所有, 而search和match只匹配一次

        """
        pattern = re.compile(r'\d+')
        result1 = pattern.findall('runoob 123 goole 456')
        result2 = pattern.findall('run88oob123google456', 0, 10)

        pass

    def test_find_iter(self):
        """
        迭代器 <= re.finditer(pattern, string, flags=0)

        """
        # it: <callable_iterator>
        it = re.finditer(r"\d+", "12a32bc43jf3")
        results = []  # ['12', '32', '43', '3']
        for match in it:
            val = match.group()
            results.append(val)
        pass

    def test_sub(self):
        """
        用于替换字符串中的匹配项
        返回 替换后的字符串 <= re.sub(
            pattern,
            repl,  1, 要替换的字符串  2 也可以是一个函数
            string,
            count=0, 模式匹配后,替换的最大次数, 0 - 表示替换所有的匹配
            flags=0
            )

        """
        phone = '2004-959-559 # 这是一个外国的号码'
        # 删除字符串中的注释
        num = re.sub(r"#.*$", "", phone)
        print("电话号码是{}".format(num))
        # 删除非数字的字符串
        num2 = re.sub(r"\D", "", phone)
        print("电话号码是: {}".format(num))

        pass

    def test_split(self):
        """
        按照匹配的子串分割字符串, 返回分割后的列表
        [..] < = re.split(
            pattern,
            string,
            [maxsplit=0, 分隔的次数,默认为0, 不限次数
            flags=0,]
            )
        """
        tsr = 'runobj, runoob, runoob.'
        # ret = ['runobj', 'runoob', 'runoob']
        ret = re.split(r"\W+", tsr)
        print(ret)
        pass
    
    def test_compile(self):
        """
        作用: 用于编译正则表达式, 生成一个正则表达式对象(Pattern), 供match() search()两个函数使用
        Pattern对象 < = compile(pattern, flags)

        re.I  忽略大小写
        re.M  多行模式
        re.S    . 包含换行符在内的任意字符
        re.X 为了增加可读性,忽略空格和#后面的注释

        re.L  表示特殊字符集\w \W \b \B \s \S依赖于当期环境
        re.U    表示特殊字符集\w \W \b \B \d \D \s \S 依赖于Unicode字符属性数据库

        匹配成功后返回一个Match对象, 它的方法有
        group([1, 2, 3, ...])
            用于获得一个或者多个匹配的字符串
        group(0) == group()  获得整个匹配的子串
        start([group])
            用于获取分组匹配的子串在整个字符串中的起始位置(子串第一个字符的索引), 默认为0
        end([group])
            .....结束位置(子串最后一个字符的索引位置+1), 默认为0
        span([group])
            返回( start(group), end(group) )


        """

    def test_tanlou(self):
        """
        python 的数量词默认是贪婪(tanlan)的, 总是匹配尽可能多的字符
        * ? + {m,n}
        在 此后面加上? 是贪婪变成非贪婪

        """
        v1 = re.match(r"aa(\d+)", 'aa2343ddd').group(1)   # 2343
        v2 = re.match(r"aa(\d+?)", 'aa2343ddd').group(1)   # 2
        v22 = re.match(r"aa(\d??)", 'aa2343ddd').group(1)   # ''
        v3 = re.match(r"aa(\d+)ddd", 'aa2343ddd').group(1)   # 2343
        v4 = re.match(r"aa(\d+?)ddd", 'aa2343ddd').group(1)   # 2343
        # 中间能匹配完么? 不能匹配完结果就是None
        v5 = re.match(r"aa(\d{2})ddd", 'aa2343ddd')   # None
        # 后限定ddd后面还有一个ddd, 如果贪婪模式就匹配到后面那个ddd
        v6 = re.match(r"aa(\w+)ddd", 'aa2343ddd909ddd').group(1)   # 2343ddd909
        # 如果是懒惰模式就匹配到第一个ddd
        v7 = re.match(r"aa(\w+?)ddd", 'aa2343ddd909ddd').group(1)   # 2343
        pass



if __name__ == '__main__':
    unittest.main()