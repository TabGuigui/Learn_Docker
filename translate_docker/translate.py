# -*- encoding: utf-8 -*-
'''
Filename         :translate.py
Description      :爬取翻译内容
Time             :2021/04/13 10:08:37
Author           :tab gui
Version          :1.0
'''


import json
import urllib.request
import urllib.parse

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

str_input = input('请输入: ')
data = {
    'i' : str_input,
    'from' : 'auto',
    'to' : 'auto',
    'smartresult' : 'dict',
    'client' : 'fanyideskweb',
    'salt' : '16057996372935',
    'sign' : '0965172abb459f8c7a791df4184bf51c',
    'lts' : '1605799637293',
    'bv' : 'f7d97c24a497388db1420108e6c3537b',
    "doctype" : 'json',
    'version' : '2.1',
    'kerfrom' : 'fanyi.web',
    'action' : 'fy_by_reatlme',
}


data = urllib.parse.urlencode(data).encode('utf-8')

response = urllib.request.urlopen(url,data)
html = response.read().decode('utf-8')
result = json.loads(html)['translateResult'][0][0]['tgt']
print('翻译结果是：', result)

