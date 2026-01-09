#math functions


import numpy as np

iArr = np.array([11,21,51,101])

iBrr = np.array([11,23,43,101])

bResult = (iArr ==iBrr)
print(bResult)

bResult = (iArr <iBrr)
print(bResult)

bResult = (iArr > iBrr)
print(bResult)

bResult = (iArr!=iBrr)
print(bResult)