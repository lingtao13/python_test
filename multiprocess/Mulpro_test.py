#!/usr/bin/python
# _*_ coding:utf-8 _*_
from datetime import datetime

__author__ = 'nelson'
__date__ = '2018/8/28 下午4:44'

from multiprocessing import Process,Pool
import datatime,random,sys,os,pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123', db='queue_thread')
cur = conn.cursor()
sql = "insert into threadtest(id,id2,id3) VALUES (%s,%s,%s)"


def mysql_insert(x):
    cur.executemany(sql,x)


def read_line(lines, mysql_insert):
    insertlist=[]
    for i in lines:
        insertlist.append(i.split('\t'))
    mysql_insert(insertlist)



if __name__ == "__main__":
    f=open('/Users/nelsonpeng/Downloads/qtfyt.txt')
    p=Pool(1)
    start = datetime.now()
    count=0
    contentlist = []
    while True:
        count+=1
        content=f.readline()
        if content=="":
            break
        contentlist.append(content)
        if len(contentlist)>19:
            p.apply_async(read_line,args=(contentlist,read_line,))
            print(count)
            contentlist=[]
    p.close()
    p.join()
    conn.commit()
    end = datetime.now()
    print("dequeue done and take time %s"%(end-start))
