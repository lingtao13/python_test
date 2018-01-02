# coding=utf-8


def sum(items):
    head,*tail = items
    return head+sum(tail) if tail else head

items = [1,19,2,44,53,3]
t=sum(items)
print(t)
