
def EvenOdd(iNo1):
    if((iNo1 % 2)==0):
        print("Given number is even")

    else:
        print("Odd number")


def main():
    print("Enter the number: ")
    iValue1 = int(input())

    EvenOdd(iValue1)


main()