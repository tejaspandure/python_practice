

def Display(iCnt):

    i = 0

    if(iCnt<=0):
        print("Invalid input")
        return 
    
    for i in range(iCnt):
        print("Jay Ganesh")


def main():

    print("enter the number: ")
    iNo = int(input())
    Display(iNo)


if __name__ == "__main__":
    main()