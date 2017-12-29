import xlrd,math
# -*- coding: UTF-8 -*-
file = '/Users/nelsonpeng/Downloads/ICBC1.xlsx'
wb = xlrd.open_workbook(filename=file)
ws = wb.sheet_by_name('TRD_Dalyr')
sgn = lambda x: 1 if x > 0 else -1 if x < 0 else 0
#Yt的取值取反

#print(dataset)

def Nadaraya( x ):
    dataset = []
    date = [i for i in range(1, 36)]
    # Xt的取值

    for r in range(0, 35):
        '''col=[]
        for c in range(3):
        col.append(ws.cell(r,c).value)'''
        dataset.append(ws.cell(r, 2).value)
        # Yt的取值(倒序)

    print(dataset)
    upper = 0
    lower = 0
    for i in range(35):
        upper = upper + kernal(x-date[i])*dataset[i]
        # 上方数值为upper
        lower = lower + kernal(x-date[i])
        # 下方数值为lower
    result = upper/lower
    return result

def kernal( x ):
    # k为kernal(Kt)
    h=0.5
    #h为自取系数
    coef = 1/(h*math.sqrt(2*math.pi))
    exp = math.pow(math.e,-(x*x)/(2*h*h))
    result = coef*exp
    return result

#test 测试
i=0
jzd =[]
for x in range(0,35):
    y1=sgn((Nadaraya(x+0.001)-Nadaraya(x-0.001))*500)
    print("第",x,"天的值是",'%.4f'%Nadaraya(x),"导数是",y1)
for x in range(1,36):
    y=y1
    y1=sgn((Nadaraya(x+0.001)-Nadaraya(x-0.001))*500)
    #  0代表极小值，1代表极大值
    if y<y1:
        i+=1
        jzd.append([x-1,0])
        print("极值点",x-1,"i=",i)
    elif y>y1:
        i+=1
        jzd.append([x-1,1])
        print("极值点", x - 1, "i=", i)
del jzd[0]
print(jzd)
dataset = []
for r in range(1, 36):
    dataset.append(ws.cell(r, 2).value)
dataset.reverse()


def lik(list):
    a = (dataset[list[0][0]]+dataset[list[4][0]])/2
    b = (dataset[list[1][0]]+dataset[list[3][0]])/2
    if list[0][1]==1 and dataset[list[2][0]]>dataset[list[0][0]] and dataset[list[2][0]]>dataset[list[4][0]] and abs(dataset[list[0][0]]-a)<a*0.015 \
            and abs(dataset[list[4][0]]-a)<a*0.015 and abs(dataset[list[1][0]]-b)<b*0.015 and abs(dataset[list[3][0]]-b)<b*0.015:
        print(list[4][0],dataset[list[4][0]+3])
    else:
        print("none")


length = len(jzd)
for x in range(length-4):
    lik(jzd[x+0:x+5])

for x in range(20):print(x)



#x=2    21.475890485118498
#x=2.01 21.474753629508573



