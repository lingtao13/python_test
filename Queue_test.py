#!/usr/bin/python
# _*_ coding:utf-8 _*_
__author__ = 'nelson'
__date__ = '2018/8/23 上午8:52'
import threading
import queue
from datetime import datetime
event=threading.Event()
import pymysql


def insert_queue(queue):
    a=0
    f=open('/Users/nelsonpeng/Downloads/qtfyt.txt')
    while True:
        i=f.readline().split('\t')
        if i==['']:
            if a<20:
                f.close()
                a+=1
                f = open('/Users/nelsonpeng/Downloads/qtfyt.txt')
                i = f.readline().split('\t')
            else:
                event.set()
                break
        queue.put(i)
        print("insert %s to the queue"%(i))
        print("the queue total size: %s"%(queue.qsize()))
    print("task done")


def dequeue(queue,i):
    conn=pymysql.connect(host='127.0.0.1',port=3306, user='root',password='123',db='queue_thread')
    cur=conn.cursor()
    sql="insert into threadtest(id,id2,id3) VALUES (%s,%s,%s)"
    start=datetime.now()
    push_list=[]
    while True:
        if event._flag:
            if queue.empty():
                break
        a=queue.get()
        cur.execute(sql,a)
    conn.commit()
    end = datetime.now()
    print("dequeue done and take time %s"%(end-start))


if __name__ == "__main__":
    q=queue.Queue()
    t1 = threading.Thread(target=insert_queue, args=(q,))
    t2 = threading.Thread(target=dequeue, args=(q, 2))
    # t3 = threading.Thread(target=dequeue, args=(q, 3))
    # t4 = threading.Thread(target=dequeue, args=(q, 4))
    for t in [t1, t2]:
        t.start()
    q.join()
    # for t in [t1, t2, t3, t4]:
    #     t.join()



