# _*_ coding:utf-8 _*_
__author__ = 'nelson'
__date__ = '2018/3/27 下午6:06'

a = ['admit','amide','bussy','balmy','begot','canal','chess','divas','dodgy','fancy','focus','games']
b1=[]
b2=[]
a1 = input()
for i in a1:
    b1.append(i)
a2 = input()
for i in a2:
    b2.append(i)


for i in a:
    if i[0] in a1 and i[1] in a2:
        print(i)


