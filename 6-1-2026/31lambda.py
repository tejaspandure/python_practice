
def ChkEven(iNo):
    if((iNo%2)==0):
        return True
    else:
        return False

def main():
    iValue = int(input("Enter teh number: "))
    iRet = ChkEven(iValue)
    if(iRet == True):
        print("Numbe is Even")
    else:
        print("Number is odd")


if __name__ == "__main__":
    main()