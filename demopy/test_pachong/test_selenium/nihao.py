# import selenium 
import time 
from selenium import webdriver
from ip.pack.log import logger
# from selenium.webdriver.common.keys import Keys 

# options = webdriver.ChromeOptions()
# options.binary_location = r'C:\Users\w3986\AppData\Local\Google\Chrome\Application\chrome.exe --profile-directory="Default"'
# driver = webdriver.Chrome(chrome_options=options)


url = 'https://www.baidu.com'

# path = "d:\python\chromedriver_win32\chromedriver.exe"
# driver = webdriver.Chrome(path)

path = "d:\python\edgedriver_win64\msedgedriver.exe"
driver = webdriver.Edge(path)
driver.get(url)
logger.info("url is open :  % s" % url)

time.sleep(5)
# driver.quit()
# logger.info("chrome driver is quit")


def test_find():
   element =  driver.find_element_by_link_text("新闻")
   logger.info("element is %s" % element) 
   logger.info("element type is %s" % type(element))
   if element:
       logger.info("element is click")
       element.click()

       
test_find()

