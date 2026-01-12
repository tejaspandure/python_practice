from time import time,ctime,localtime

epoch = time()
print(epoch)

epoch = ctime()
print(epoch)

epoch = localtime()
print(epoch)

print()
print()

stobj = localtime()
print(stobj.tm_mday, end="/")
print(stobj.tm_mon, end="/")
print(stobj.tm_year)

print()
print()

stobj = localtime()
print(stobj.tm_hour,end=":")
print(stobj.tm_min,end=":")
print(stobj.tm_sec)