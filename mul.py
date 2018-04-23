#!/usr/bin/python
# _*_ coding:utf-8 _*_
__author__ = 'nelson'
__date__ = '2018/4/19 下午1:58'


from multiprocessing import Process
import os

from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
def one():
    os.system("python3 ./1.py")
def two():
    os.system("python3 ./2.py")
def thr():
    os.system("python3 ./3.py")
# BlockingScheduler
def one_sch():
    scheduler = BlockingScheduler()
    scheduler.add_job(one, 'cron', day_of_week='1-5', hour=15, minute=39)
    scheduler.start()

if __name__ == "__main__":
    p1 = Process(target=one_sch)  #申请子进程
    p2 = Process(target=two)
    p3 = Process(target=thr)
    p1.start() #运行进程
    p2.start()
    p3.start()