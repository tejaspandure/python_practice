from functools import reduce

CheckEven = lambda No : (No % 2 == 0)

Increase = lambda No : (No + 1)

Add = lambda A,B:(A+B)

def main():

    Data  = []

    print("Enter the no of elements: ")
    iValue = int(input())

    print("Enter the elements: ")
    iCnt = 0

    for iCnt in range(0,iValue):
        iNo = int(input())
        Data.append(iNo)

    FData = list(filter(CheckEven,Data))
    print("Data after filter activity: ",FData)

    MData = list(filter(Increase,FData))
    print("Data after teh Map activity. ",MData)

    RData = reduce(Add,MData)
    print("data after reduce activity: ",RData)


if __name__ == "__main__":
    main()