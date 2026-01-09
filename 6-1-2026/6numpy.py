#zeros()

import numpy as np

iArr = np.zeros(5)

for iCnt in iArr:
    print(iCnt)


iStart = 0
iEnd = len(iArr)

for iCnt in range(iEnd):
    print(iArr[iCnt])


iStart = 0
iEnd = len(iArr)

while(iStart<iEnd):
    print(iArr[iStart])
    iStart+=1
    