# passing array tp function

from array import *

def show(iArr):
    print(iArr)
    print(type(iArr))
    for iCnt in iArr:
        print(iCnt)
        


def main():
    a = array('i',[11,21,41,51,61])
    show(a)


if __name__ == "__main__":
    main()