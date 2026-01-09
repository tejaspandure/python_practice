import numpy as np

iArr = np.array([11,21,51,101])
iBrr = np.array([11,21,51,332])

iResult = (iArr ==iBrr)
print(any(iResult))


iResult=(iArr ==iBrr)
print(all(iResult))