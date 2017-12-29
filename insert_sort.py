def insert_sort(list):

    count = len(list)
    for i in range(1,count):
        key = list[i]
        j=i-1
        while j>=0:
            if list[j]>key:
                list[j+1]=list[j]
                list[j]=key
            j -=1
    return list

def shell_sort(list):
    count = len(list)
    step = 2
    group = count/step
    while group > 0:
        j = i + group


a = [2, 3, 5, 1, 6, 21, 67, 24]
b=insert_sort(a)
print(b)

