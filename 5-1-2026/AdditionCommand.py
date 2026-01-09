
def Addition(iNo1, iNo2):
    iAns = None
    iAns = iNo1 + iNo2
    return iAns


def main():
    print("Enter the number: ")
    iValue1 = int(input())

    print("Enter the number: ")
    iValue2 = int(input())

    iResult = Addition(iValue1, iValue2)
    print("Addition is: ",iResult)


if __name__ == "__main__":
    main()