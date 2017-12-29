def cmp(a, b):
    ab = int(a+b)
    ba = int(b+a)
    return 1 if ab > ba else -1
num = input()
l=input().split(' ')
l.sort(key=cmp, reverse=True)
print(int(''.join(l)))
