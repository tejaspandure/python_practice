#logspace()

import numpy as np

a = np.logspace(1,3,5)

i = 0

for i in a:
    print(i)

iEnd = len(a)
iStart = 0

for iStart in range(iEnd):
    print(a[iStart])

iEnd = len(a)
iStart = 0
while(iStart<iEnd):
    print(a[iStart])
    iStart+=1