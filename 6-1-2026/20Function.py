

def add(iNo1, iNo2):
    iC = iNo1 + iNo2
    return iC

def main():
    iValue1 = int(input("Enter the first number: "))
    iValue2 = int(input("Enter the second value : "))
    iRet =0
    iRet = add(iValue1,iValue2)
    print("Addition is: %d" %iRet)

if __name__ == "__main__":
    main()