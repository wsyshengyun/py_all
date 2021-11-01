# -*- coding: utf-8 -*-
'''
@File    :   some.py
@Time    :   2020/09/26 10:37:36
'''


import requests   

headers = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"h-CN,zh;q=0.9",
    "Cache-Control":"max-age=0",
    "Connection":"keep-alive",
    "Content-Length":"116",
    "Content-Type":"application/x-www-form-urlencoded",
    "Cookie":"lang=chs; sid=rhzpbyvoDxQlGjch; lsid=jrnQeJaLZyBOnGtb",
    "Host":"192.168.1.1",
    "Origin":"http://192.168.1.1",
    "Referer":"http://192.168.1.1/macfilter.cgi",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
}

url = "http://192.168.1.1/macfilter.cgi?add"
formm = {
      "csrf_token": "JDmWcqYEYAlzQsmk"
    , "mac_filter_enable": "enable"
    , "mac_exclude_mod": "BLOCKED"
    , "mac_address": "88:5a:06:a3:32:5d"
}
headers2 = {
"Referer": "http://192.168.1.1/macfilter.cgi",
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
}

urls = [
    "http://192.168.1.1/macfilter.cgi", 
    "http://192.168.1.1/js_cu/jquery-1.6.1.min.js", 
    "http://192.168.1.1/js_cu/global.js", 
    "http://192.168.1.1/css/cu_smart.css" 
]

req = requests.post(url, data=formm, headers = headers)
print(req.encoding)
print(req.status_code)

for url in urls:
    res = requests.get(url, headers = headers2)
    print(req.status_code)

