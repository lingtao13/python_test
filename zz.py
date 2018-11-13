#!/usr/bin/python
# _*_ coding:utf-8 _*_
__author__ = 'nelson'
__date__ = '2018/8/18 下午11:10'

#
# 创建list
# list1=[]
#
# # 向列表里插入数据
# for i in range(1000,2001):
#     list1=list1+[i]
#
#
# # 切片 保留整十年
# print(list1)
# list1=list1[::10]
# print(list1)


# # 编写函数，判断是否为闰年
# def isleap(a):
#     if a%4==0 and a%100!=0:
#         return 1
#     elif a%400==0:
#         return 1
#     else:
#         return 0
#
# list2=[]
#
#
# # 迭代留下所有list1中的闰年
# for i in list1:
#     if isleap(i):
#         list2=list2+[i]
#     else:
#         pass

# print(list2)

a=[1,2,2,2,3,4,2,3,6,5,6]
# for i in range(len(a)):
#     if a[i]!=a[i-1]:
#         print(a[i-1])
#         print(a[i])
# a1=list(set(a))
# a1.sort(key=a)
# print(a1)
map={1:"a",2:"b",3:"c",4:"d",5:"e",6:"f"}

for i in range(len(a)):
    a[i]=map[a[i]]
print(a)



