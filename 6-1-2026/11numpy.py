# view()
import numpy as np

iArr = np.array([10,20,30,40,50])
iBrr = iArr.view()

print(iArr)
print(iBrr)

print("iArr",id(iArr))
print("iBrr",id(iBrr))


#copy()

iCrr = np.array([20,23,42,31,11])
iDrr = np.copy(iCrr)

print(iCrr)
print(iDrr)

print("iCrr",id(iCrr))
print("iDrr",id(iDrr))

