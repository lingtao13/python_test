#!/usr/bin/python
# _*_ coding:utf-8 _*_
__author__ = 'nelson'
__date__ = '2018/8/15 下午3:04'


from random import random
import math
count=0

for i in range(2000):
    x,y=random(),random()
    dic=math.sqrt(x**2+y**2)
    if dic<=1:
        count=count+1
pi=4*(count/2000)
print(pi)



list=[]
for i in range(3,101):
    list.append(i)
    for j in range(2,i):
        if (i%j==0):
            list.remove(i)
            break
        else:
            pass
print(list)

list1=[1,2,3,4,"123123"]
print(list1[4][:-2])
