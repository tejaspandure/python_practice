#arange()

import numpy as np

iArr = np.arange(1,10,2) 

for i in iArr:
    print(i)





iStart = 0
iEnd = len(iArr)

for iCnt in range(iEnd):
    print(iArr[iCnt])





iStart = 0
iEnd = len(iArr)

while(iStart<iEnd):
    print(iArr[iStart])
    iStart+=1

