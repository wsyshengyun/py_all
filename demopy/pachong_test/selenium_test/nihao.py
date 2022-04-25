# import selenium 
from selenium import webdriver

# from selenium.webdriver.common.keys import Keys
from ...logger.log import logger

url = 'https://www.baidu.com'
path = "d:\python\edgedriver_win64\msedgedriver.exe"


class MySelenium(object):
    def __init__(self, path, url):
        self.driver_path = path
        self.url = url
        self.init()
        pass

    def init(self):
        self.driver = webdriver.Edge(self.driver_path)
        self.driver.get(self.url)
        logger.info('url {} is open.'.format(self.url))

    def test_find(self):
        element = self.driver.find_element_by_link_text("新闻")
        logger.info("type 新闻 element is :{}".format(type(element)))
        if element:
            element.click()


def test():
    obj = MySelenium(path, url)
    obj.test_find()

# test()
