import numpy as np

def show(iArr):
    print(iArr)
    print(type(iArr))
    for iCnt in iArr:
        print(iCnt)

    return iArr


def main():
    iArr = np.array([11,21,51,101])
    iRet = show(iArr)
    print(iRet)



if __name__ == "__main__":
    main()