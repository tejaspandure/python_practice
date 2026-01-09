from functools import reduce

checkEven = lambda No : (No % 2 ==0)

Increase = lambda No : (No + 1)

Add = lambda A,B : (A+B)




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