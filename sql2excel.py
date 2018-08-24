# _*_ coding:utf-8 _*_
import xlwt

fopen=open('/Users/nelsonpeng/Downloads/loan2015.txt','r',encoding='utf-8')
lines=fopen.readlines()
file=xlwt.Workbook(encoding='utf-8',style_compression=0)
sheet=file.add_sheet('data')
i=0
for line in lines:
    a=line.split('|')
    for b in range(len(a)):
        sheet.write(i,b,a[b])
    i=i+1
file.save('loan2015.xls')