# _*_ coding:utf-8 _*_
__author__ = 'nelson'
__date__ = '2018/4/11 上午10:47'

def recurse(list,left,right):
    if left<right:
        i=left
        j=right
        tmp=list[left]
        while(i<j):
            while(i<j and list[j]>=tmp):
                j=j-1
            if i<j:
                list[i]=list[j]
                i=i+1
            while(i<j and list[i]<tmp):
                i=i+1
            if i<j:
                list[j]=list[i]
                j=j-1
        list[i]=tmp
        recurse(list,left,i-1)
        recurse(list,i+1,right)
    return list

def quicksort(list):
    leng=len(list)
    recurse(list,0,leng-1)

list = [1,4,6,23,45,68,22,14,3]
quicksort(list)
print(list)


def merge(left, right):
    i, j = 0, 0
    result = []
    while (i < len(left) and j < len(right)):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def merge_sort(list):
    if len(list) <= 1:
        return list
    num = len(list) // 2  # python3 整数除法/会变浮点，改为//8
    left = merge_sort(list[:num])
    right = merge_sort(list[num:])
    return merge(left, right)

list=[2,42,13,57,24,1,66,43]
b = merge_sort(list)
print(b)

