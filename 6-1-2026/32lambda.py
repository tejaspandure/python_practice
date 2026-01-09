
def ChkEven(iNo):
    return (iNo%2==0)

ChkEvenX = lambda iA: (iA % 2 ==0)
        

def main():
    iValue = int(input("Enter teh number: "))
    iRet = ChkEven(iValue)
    if(iRet == True):
        print("Numbe is Even")
    else:
        print("Number is odd")


if __name__ == "__main__":
    main()