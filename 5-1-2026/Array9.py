from array import * 

roll = [11,21,41,51]
roll1 = [53,66,44,89]

iStart = 0
iEnd = len(roll)

while(iStart<iEnd):
    print(roll[iStart])
    iStart+=1

print("After extended")
roll.extend(roll1)

iStart = 0
iEnd = len(roll)

while(iStart<iEnd):
    print(roll[iStart])
    iStart+=1


