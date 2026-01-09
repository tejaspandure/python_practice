
def Display(iCnt):

    i = 0

    if(iCnt<=0):
        print("Invalid input : ")
        return
    
    while(iCnt>i):
        print("Jay Ganesh",end=" ")
        i = i+1


def main():
    print("Enter the frequncy: ")
    iValue = int(input())
    Display(iValue)


if __name__ == "__main__":
    main()