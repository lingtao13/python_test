# coding:utf-8
#对于类学习巩固，尤其是self的加深理解

def decorate(fun):
    def wrapper(a):
        print("hello,我要活动一下")
        fun(a)
        print("好的，我活动完了")
    return wrapper


class movement:
    def __init__(self,num):
        self.name = num

    def singing(self):
        print("我要唱歌")

    @decorate
    def dancing(self):
        print("我要跳舞")




abc = movement("abc")

abc.dancing()
