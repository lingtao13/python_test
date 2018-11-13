#!/usr/bin/python
# _*_ coding:utf-8 _*_
__author__ = 'nelson'
__date__ = '2018/8/15 下午3:04'


import math
from json import dumps,loads

a="[{name:1},{name:2},{name:3}]"
jsons2=loads(a)
print(jsons2)
b=a.strip("[]").split(",")
print(b)
d=[]

for i in b:
    c=loads(i)
    d.append(c)

print(d)
jsons=dumps(d)
print(jsons)
m=[]

for n in d:
    e=dumps(n)
    m.append(e)

x=",".join(m)
x='['+x+']'

print(x)