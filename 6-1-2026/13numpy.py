#2D array
import numpy as np

iArr = np.array([[11,21,31,41,51],
                 [22,3,4,33,4]])

iStart = 0
iEnd = len(iArr)

for iStart in range(iEnd):
    print(iArr[iStart])
    iStart+=1

iRow = int(input("Enter the frequency of rows: "))
iCol = int(input("Enter teh frequency of columns: "))

iBrr = np.zeros((iRow,iCol),dtype=int)
iCnt = 0
jCnt = 0

for iCnt in range(iRow):
    for jCnt in range(iCol):
        iBrr[iCnt][jCnt] = int(input("Enter the elements : "))


for i in range(iRow):
    print(iBrr[i])
    

