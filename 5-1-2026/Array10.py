from array import *

roll = array('i',[10,20,30,40,50])

iStart = 0
iEnd = len(roll)

while(iStart<iEnd):
    print(roll[iStart])
    iStart+=1


print("*********************************************************************")

iStart = 0
iA = roll[1:3]

for i in iA:
    print(roll[iStart])
    iStart+=1