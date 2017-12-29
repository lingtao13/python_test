# a = "xiao mi shou ji".split(' ')
# print(' '.join(a[::-1]))
#  split 输出列表
#
# b=[1,2,3,4,5,6,7,8,9]
# b[2:0]=[99]
# # del b[2:3]
# print(b[2:3])
number = input()
list = input().split(' ')
len1 = len(list)
for i in range(len1):
    num = int(list[i])
    yueshu = 0
    for x in range(1,num+1):
        if(num % x ==0):
            yueshu+=1
    print(yueshu)