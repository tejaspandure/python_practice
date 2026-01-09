import numpy as np

iValue = int(input("Enter the frequency: "))

iA = np.zeros(iValue, dtype=int)

for iCnt in range(len(iA)):
    print("Enter the elements: ")
    iX = int(input())
    iA[iCnt] = iX

for iCnt in range(len(iA)):
    print(iA[iCnt])



iValue1 = int(input("Enter teh frequency: "))
iBrr = np.zeros(iValue1,dtype=int)
iCnt = 0

while(iCnt< (len(iBrr))):
    print("Enter teh elements: ")
    iY = int(input())
    iBrr[iCnt] = iY
    iCnt+=1
    
jCnt = 0

while (jCnt<(len(iBrr))):
    print(iBrr[jCnt])
    jCnt+=1
