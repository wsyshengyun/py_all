# coding:utf8


from abc import ABCMeta, abstractmethod
import os


class Page:
    def __init__(self, page_num):
        """ """
        self.__pageNum = page_num

    def getCount(self):
        return "第 " + str(self.__pageNum) + "页内容..."


class Catalogue:
    def __init__(self, title):
        """ """
        self.__title = title
        self.__chapters = []

    def add_chapter(self, title):
        self.__chapters.append(title)

    def show_info(self):
        """

        """
        print(f"书名: {self.__title}")
        print(f"目录: ")
        for chapter in self.__chapters:
            print(f"    {chapter}")


class IBook(metaclass=ABCMeta):
    @abstractmethod
    def parseFile(self, filepath):
        pass

    @abstractmethod
    def getCatalogue(self):
        """

        """
        pass

    @abstractmethod
    def getPageCount(self):
        """

        """
        pass

    @abstractmethod
    def getPage(self, pageNum):
        """

        """
        pass


class TxtBook(IBook):

    def parseFile(self, filepath):
        print(f"{filepath}文件解析成功")
        self.__title = os.path.splitext(filepath)[0]
        self.__pagecount = 500
        return True

    def getCatalogue(self):
        catalogue = Catalogue(self.__title)
        catalogue.add_chapter("第一章 标题")
        catalogue.add_chapter("第二章 标题")
        return catalogue

    def getPage(self, pageNum):
        return Page(pageNum)

    def getPageCount(self):
        return self.__pagecount


class EpubBook(IBook):

    def parseFile(self, filepath):
        print(f"{filepath}文件解析成功")
        self.__title = os.path.splitext(filepath)[0]
        self.__pagecount = 800
        return True

    def getCatalogue(self):
        catalogue = Catalogue(self.__title)
        catalogue.add_chapter("第一章 标题")
        catalogue.add_chapter("第二章 标题")
        return catalogue
        pass

    def getPage(self, pageNum):
        return Page(pageNum)

    def getPageCount(self):
        return self.__pagecount


class Outline:
    def __init__(self):
        """ """
        self.__outlines = []

    def addOutline(self, title):
        self.__outlines.append(title)

    def getOutline(self):
        return self.__outlines


class PdfPage:
    def __init__(self, pageNum):
        """ """
        self.__pageNum = pageNum

    def getPageNum(self):
        return self.__pageNum


class ThirdPdf:
    def __init__(self):
        """ """
        self.__pageSize = 0
        self.__title = ""

    def open(self, filePath):
        print(f"第三方库解析PDF文件: {filePath}")
        self.__title = os.path.splitext(filePath)[0]
        self.__pageSize = 1000
        return True

    def getTitle(self):
        return self.__title

    def getOutline(self):
        outline = Outline()
        outline.addOutline("第一章 PDF电子书标题")
        outline.addOutline("第二章 PDF电子书标题")

        return outline

    def pageSize(self):
        return self.__pageSize

    def page(self, index):
        return PdfPage(index)


class PdfAdapterBook(ThirdPdf, IBook):
    def __init__(self, thirdPdf):
        """ """
        self.__thirdPdf = thirdPdf

    def parseFile(self, filepath):
        rtn = self.__thirdPdf.open(filepath)
        if rtn:
            print(filepath + "文件解析成功")
        return rtn


    def getCatalogue(self):
        outline = self.getOutline()
        print("将outline结构的目录转换成Catalogue结构目录")
        catalogue = Catalogue(self.__thirdPdf.getTitle())
        for title in outline.getOutline():
            catalogue.add_chapter(title)
        return catalogue

    def getPageCount(self):
        return self.__thirdPdf.pageSize()

    def getPage(self, pageNum):
        page = self.page(pageNum)
        print("将PdfPage的面对象转换成Page的对象")
        return Page(page.getPageNum())


class Reader:
    def __init__(self, name):
        """ """
        self.__name = name
        self.__filePath = ""
        self.__curBook = None
        self.__curPageNum = -1

    def __initBook(self, filePath):
        self.__filePath = filePath
        extName = os.path.splitext(filePath)[1]
        if extName.lower() == ".epub":
            self.__curBook = EpubBook()
        elif extName.lower() == '.txt':
            self.__curBook = TxtBook()
        elif extName.lower() == '.pdf':
            self.__curBook = PdfAdapterBook(ThirdPdf())
        else:
            self.__curBook = None

    def openFile(self, filePath):
        self.__initBook(filePath)
        if self.__curBook is not None:
            rtn = self.__curBook.parseFile(filePath)
            if rtn:
                self.__curPageNum = 1
            return rtn
        return False

    def closeFile(self):
        print(f"关闭 {self.__filePath} 文件")
        return True

    def showCatalogue(self):
        catalogue = self.__curBook.getCatalogue()
        catalogue.show_info()

    def prePage(self):
        print("往前翻一页: ", end='')
        return self.gotoPage(self.__curPageNum-1)

    def nextPage(self):
        print("往后翻一页: ", end='')
        return self.gotoPage(self.__curPageNum+1)

    def gotoPage(self, pageNum):
        if pageNum>1 and pageNum<self.__curBook.getPageCount()-1:
            self.__curPageNum = pageNum

        print(f"显示第 {self.__curPageNum} 页")
        page = self.__curBook.getPage(self.__curPageNum)
        page.getCount()
        return page


def testReader():
    reader = Reader("阅读器")
    if not reader.openFile("平凡的世界.txt"):
        return
    reader.showCatalogue()
    reader.prePage()
    reader.nextPage()
    reader.nextPage()
    reader.closeFile()
    print()
    if not reader.openFile("追风筝的人.epub"):
        return
    reader.showCatalogue()
    reader.nextPage()
    reader.nextPage()
    reader.closeFile()
    print()

    if not reader.openFile(("如何从生活中领悟设计.pdf")):
        return  None

    reader.showCatalogue()
    reader.nextPage()
    reader.nextPage()
    reader.closeFile()


if __name__ == '__main__':
    testReader()










