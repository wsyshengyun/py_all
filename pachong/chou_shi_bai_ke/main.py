# -*- coding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2020/09/22 22:19:24
'''
import urllib 
# import urllib2 
import requests
import time
from lxml import etree 

url = ' http://www.qiushibaike.com/hot/page/'

class Save(object):
    def __init__(self, dirpath, num=1):
        self.dirpath = dirpath 
        self.get_path(num)
    
    def get_path(self, num):
        self.path_ok = self.dirpath +  str(num) + '.txt'
    
    def save(self, num, text):
        self.get_path(num)
        with open(self.path_ok, 'w', encoding='utf-8') as target:
            target.write(text)




class Main(object):
    def __init__(self, url):
        self.url = url 
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent':user_agent}
        self.page = 1
        self.saveobj = Save(dirpath='./')
        
    def get_url(self):
        self.target_url = self.url + str(self.page)

    def get_response(self):
        self.get_url()
        response = requests.get(self.target_url, headers = self.headers)
        return response 
    
    def parse(self):
        response = self.get_response()
        phtml = etree.HTML(response.text) 
        result = phtml.xpath("//div[@class='content']//span/text()")
        text = ''
        for ele in result:
            if ele == "":
                continue
            text += ele.lstrip()
            text += '\r\n'
        return text
  

    def save_some_page(self, all_num=1):
        for _ in range(all_num):
            text = self.parse()
            self.saveobj.save(self.page, text)
            self.page += 1
            time.sleep(1)
            # for ele in result:

def main():
    obj = Main(url) 
    obj.save_some_page(10)

if __name__ == '__main__':
    main()
    
        