import array as arr
def show(iArr):
    print(iArr)
    print(type(iArr))
    for iCnt in iArr:
        print(iCnt)

    return iArr

def main():
    a = arr.array('i',[11,21,41,51,101])
    iRet = show(a)
    print(iRet)

if __name__ == "__main__":
    main()