
import numpy as np

iRow = int(input("Entr teh rows: "))
iCol = int(input("enter teh columns : "))

iArr = np.zeros((iRow,iCol),dtype = int)

i= 0
j= 0

for i in range(iRow):
    for j in range(iCol):
        print("Enter the elemtns: ")
        iX = int(input())
        iArr[i][j] = iX
    print()


for i in range(len(iArr)):
    print(iArr[i])


iRow1 = int(input("Entr teh rows: "))
iCol1 = int(input("enter teh columns : "))

iArr1 = np.zeros((iRow1,iCol1),dtype = int)

i = 0
j = 0

while(i<iRow1):
    while(j<iCol1):
        x = int(input("enter the elemnts: "))
        iArr1[i][j] = x
        j+=1
    i+=1

n = len(iArr1)

while (i<iRow1):
    while(j<iArr1[i]):
        print(iArr1[iRow1][iCol1])
        j+=1
    i+=1