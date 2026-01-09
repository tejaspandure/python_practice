from array import *

roll = array('i',[11,21,51,101])

i = 0
n = len(roll)

for i in range(n):
    print(roll[i])
    i+=1


print("Enter the number and the position that you want to insert: ")
iPos = int(input("Entr teh position"))
iValue = int(input("Enter the value"))

roll.insert(iPos,iValue)

n = len(roll)

for i in range(n):
    print(roll[i])
    i+=1

print("Enter the value that you want to remove: ")
iValue2 = int(input())

roll.remove(iValue2)

n = len(roll)

for i in range(n):
    print(roll[i])
    i+=1