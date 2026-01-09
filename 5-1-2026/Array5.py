from array import *

roll = array('i',[11,21,51,101,201])

n  = len(roll)
i = 0

for i in range(n):
    print(roll[i])
    i+=1


print("After append: ")
roll.append(2333)

n = len(roll)
i = 0

for i in range(n):
    print(roll[i])
    i +=1

print("after pop: ")
roll.pop(0)

n = len(roll)
i = 0

for i in range(n):
    print(roll[i])
    i+=1