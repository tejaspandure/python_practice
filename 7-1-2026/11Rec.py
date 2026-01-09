i = 1
Fact = 1

def Factorial(iNo):
    global i
    global Fact

    if(iNo>=1):
        Fact = Fact * iNo
        iNo = iNo -1
        Factorial(iNo)

    return Fact



def main():
    print("Entr the number: ")
    value = int(input())

    Ret = Factorial(value)
    print("FActorial is: ",Ret)

if __name__ == "__main__":
    main()