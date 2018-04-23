# _*_ coding:utf-8 _*_
__author__ = 'nelson'
__date__ = '2018/2/13 上午10:03'

import time
from datetime import datetime, timedelta
from time import sleep

SECONDS_PER_DAY = 24 * 60 * 60


def doFunc():
    print ("do Function...")


def doFirst():
    curTime = datetime.now()
    print (curTime)
    desTime = curTime.replace(hour=11, minute=39, second=0, microsecond=0)
    print (desTime)
    delta = desTime-curTime
    sleeptime = delta.total_seconds()
    print ("Now day must sleep %d seconds" % sleeptime)
    sleep(sleeptime)
    doFunc()


if __name__ == "__main__":
    while True:
        doFirst()
        sleep()