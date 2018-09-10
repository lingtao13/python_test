#!/usr/bin/python
# _*_ coding:utf-8 _*_
__author__ = 'nelson'
__date__ = '2018/8/31 上午9:53'


from multiprocessing import Process,Pool
import datatime,random,sys,os,pymysql
from datetime import datetime

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123', db='queue_thread')
cur = conn.cursor()
sql = "insert into threadtest(id,id2,id3) VALUES (%s,%s,%s)"


def mysql_insert(x):
    cur.execute(sql,x)


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
        p.apply_async(mysql_insert,args=(content.split('\t'),))
        if count%100==0:
            print(count)
    conn.commit()
    p.close()
    p.join()
    end = datetime.now()
    print("dequeue done and take time %s"%(end-start))
