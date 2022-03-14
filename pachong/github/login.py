# -*- coding: utf-8 -*-
'''
@File    :   login.py
@Time    :   2020/09/22 20:31:04
'''


import requests 
from lxml import etree

class Login(object):
    def __init__(self):
        print("__init__")
        self.header = {
            'Referer'  : 'https://github.com/'
            ,'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
            ,'Host':'github.com'
        }
        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        self.logined_url = 'https://github.com/settings/profile'
        self.session = requests.Session()
        

    def token(self):
        print("__token__")
        response = self.session.get(self.login_url, headers = self.header)
        selector = etree.HTML(response.text)
        # token = selector.xpath("//div/input[2]/@value")[0]
        token = selector.xpath("//div/form/input[1]/@value")[0]
        print(token)
        return token

    def login(self, email, password):
        print("__login__")
        post_data = {
            'commit':'Sign in'
            , 'utf8':'✓'
            , 'authenticity_token' : self.token() 
            , 'login':email
            , 'password': password
        }

        response = self.session.post(self.post_url, data=post_data, headers = self.header)
        if response.status_code == 200:
            text = response.text
            self.dynamics(text) 
            self.save_html(text)
    
    def save_html(self, text):
        path = './html.txt'
        with open(path, 'w', encoding='utf-8') as f:
            f.write(text)

        # response = self.session.get(self.logined_url, headers=self.header)
        # if response.status_code == 200:
        #     self.profile(response.text)
    
    def dynamics(self, html):
        print("__dynamics__")
        selector = etree.HTML(html)
        # dynamics = selector.xpath('//div[contains(@class, "news")]//div[contains(@class, "alert")]')
        dynamics = selector.xpath('//div/a[contains(@data-hovercard-type, "user")]//text()')
        for item in dynamics:
            # dynamic = ' '.join(item.xpath('.//div[@class="title"]//text()')).strip()
            # print(dynamic)
            print(item)
        pass


    def profile(self, html):
        print("__profile__")
        selector = etree.HTML(html)
        name = selector.xpath('//input[@id="user_profile_name"]/@value')[0]
        email = selector.xpath('//select[@id="user_profile_email"]/option[@value!=""]/text()')
        print(name, email)
        pass

def main():
    print("----main---")
    login = Login() 
    login.login(email='wsy8718@163.com', password='wsygit8718')

if __name__ == '__main__':
    main()
    
    