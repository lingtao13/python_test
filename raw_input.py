myDic = {'0':[1,0]}
high = 1;
nLen = int(input())
for x in range(nLen - 1):
    [key,val] = input().split(' ')
    print([key,val])
    print(myDic[key][0])
    if key in myDic and myDic[key][1] < 2:
        myDic[key][1] = myDic[key][1] + 1
        myDic[val] = [myDic[key][0] + 1, 0]
        print(myDic)
        if myDic[val][0] > high:
            high = myDic[val][0]
            pass
print(high)
