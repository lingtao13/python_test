#!/usr/bin/python
# _*_ coding:utf-8 _*_
__author__ = 'nelson'
__date__ = '2018/5/28 下午1:46'

a = [1, 3, 6, 3,1, 1]

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,14,15]

print(a[3:4])

list1 = []
for i in range(a[1]):
    for j in range(a[2 + i]):
        summary = sum(a[2:2 + i])
        list1.append([b[0], b[i + 1 + summary], b[2 + i+summary + j]])
for i in range(a[-1]):
    list1.append([b[0], 0, b[-i - 1]])

print(list1)

list=[1,2]
list[1]=1
print(list)
