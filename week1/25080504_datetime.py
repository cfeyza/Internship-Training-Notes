from datetime import datetime
#from datetime import date
#from datetime import time


print(dir(datetime))

simdi = datetime.now()
print(simdi)
x = datetime.now().year
print(x)
x = datetime.now().month
print(x)
x = datetime.now().day
print(x)
x = datetime.now().hour
print(x)
x = datetime.now().minute
print(x)
x = datetime.now().second
print(x)
x = datetime.today().year
print(x)
simdi = datetime.today()
print(x)
x = datetime.ctime(simdi)
print(x)
x = datetime.strftime(simdi, "%Y %X %d %A %B")
print(x)

t = "21 Nisan 2019"
gun, ay, yil = t.split()
t2 = "15 April 2019 hour 10:12:30"
dt = datetime.strptime(t, "%d %B %Y hour %H:%M:%S")
print(dt)
print(dt.year)
birthday = datetime(1983,5,9,12,30,10)
x = datetime.timestamp(birthday)
print(x)
x = datetime.fromtimestamp(x)
print(x)
x = datetime.fromtimestamp(0)
print(x)
x = simdi - birthday #timedelta
print(x)
print(x.days)
print(x.seconds)
print(x.microseconds)

from datetime import timedelta
x = simdi + timedelta(days=10, minutes=23)
print(x)
x = simdi - timedelta(days=10, minutes=23)
print(x)
