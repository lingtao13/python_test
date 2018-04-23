# _*_ coding:utf-8 _*_
__author__ = 'nelson'
__date__ = '2018/3/17 下午9:57'

import requests
import ssl
import urllib

URL = "https://www.qq.com/"
r1 = urllib.request.urlopen(URL).read()
print(r1)