#!/usr/bin/python
# _*_ coding:utf-8 _*_
__author__ = 'nelson'
__date__ = '2018/8/17 下午1:35'

import base64

f=open('/Users/nelsonpeng/lingtao13.github.io/img/avatar_sha256.jpg','rb')

ls_f=base64.b64encode(f.read())
f.close()
print(ls_f)