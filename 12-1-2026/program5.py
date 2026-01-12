from datetime import datetime

dobj = datetime(year = 2019, month = 6, day = 30)
dobj1 = datetime(year= 2018, month = 5, day = 29, hour = 15, minute = 34)
dobj2 = datetime(2017, 4, 28)
dobj3 = datetime(2016, 3, 10, 11, 45)

print(dobj)
print(dobj1)
print(dobj2)
print(dobj3)
print()
dobj4 = datetime.now()
print(dobj4)
dobj5 = datetime.today()
print(dobj5)
