#where()

#np.where(condition,expression1,expression2)

import numpy as np

iArr = np.array([11,0,51,101])
iBrr = np.array([10,31,22,88])

iCrr = np.where(iArr>iBrr,iArr,iBrr)
print(iCrr)

iResult = np.nonzero(iArr)
print(iResult)


