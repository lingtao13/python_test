#!/usr/bin/python
# _*_ coding:utf-8 _*_
__author__ = 'nelson'
__date__ = '2018/8/22 上午8:26'

import threading
import time
from datetime import datetime


def singing():
    time.sleep(1)
    print("I like singing")


def dancing():
    print("I don't like dancing")


def read(f):
    a=f.readline()
    print(a)


if __name__ == "__main__":
    f=open('/Users/nelsonpeng/Downloads/qtfyt.txt','r')
    start=datetime.now()
    for i in range(5):
        t=threading.Thread(target=read,args=f)
        t.start()
    end=datetime.now()
    print("total time=%s"%((end-start).seconds))