import datetime,time

today = datetime.datetime.now()
print(today)
that_day = datetime.datetime(2015,9,30)


print(today-that_day)

time1=abs((today-that_day).total_seconds())
time1 = int('%d' % time1)

print(time1)