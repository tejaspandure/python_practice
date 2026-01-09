
def setComp(iFreq):
    set1 = set()

    for iCnt in range(iFreq):
        iX = int(input("Enter teh elements: "))
        set1.add(iX)

    print(set1)


def main():
    iValue = int(input("Enter the frequency: "))
    setComp(iValue)

    set3 =  {i+1 for i in range(9)}
    print("set3",set3)

    set4 = {iCnt for iCnt in range(20) if iCnt%2==0}
    print("set4",set4)

    print("entr the range of set: ")
    iValue= int(input())
    set5 = {iCnt for iCnt in range(iValue) if iCnt % 2 == 0 if iCnt %3==0}
    print("set5",set5)

    set6 = {i if i%2 == 0 else i*10 for i in range(10)}
    print(set6)

    set7 = set()
    for i in range(50):
        if i % 2 == 0:
            set7.add(i)
        else:
            set7.add(i*10)

    print("set7",set7)

    set8 = set()
    set8 = {(iCnt,jCnt) for jCnt in range(4,5) for iCnt in range(6,8)}
    print(set8)
    print(type(set8))

    set9 = set()
    for iCnt in range(3,5):
        for jCnt in range(8,9):
            set9.add(jCnt)
        set9.add(iCnt)

    print("set9",set9)


if __name__ == "__main__":
    main()