# _*_ coding:utf-8 _*_
__author__ = 'nelson'
__date__ = '2018/3/16 下午12:57'

import threading,time

num = 0


class MyThread(threading.Thread):
    def run(self):
        global num
        temp = num
        time.sleep(0.5)
        temp += 1
        num = temp


l = []


for i in range(50):
    t = MyThread()
    t.start()
    l.append(t)

for j in l:
    j.join

print(num)