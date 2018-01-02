# coding:utf-8
a = {
    'x':1,
    'y':2,
    'z':3
}
b = {
    'w':10,
    'x':11,
    'y':2
}

c = a.keys()&b.keys()
d = a.items()&b.items()


print(c)
print(d)