from functools import reduce

def checkEven(No):
    return (No % 2 == 0)

def Increase(No):
    return No + 1

def Add(A,B):
    return A + B


def main():
    Data= [22,24,11,42,52,63,46,74,5,534,34,54]
    print("Data from input lise : ",Data)

    FData = list(filter(checkEven,Data))
    print("data after filter activity: ",FData)

    MData = list(map(Increase,FData))
    print("data after map activity: ",MData)

    RData = reduce(Add,MData)
    print("daata after reduce activity , ",RData)


if __name__ == "__main__":
    main()