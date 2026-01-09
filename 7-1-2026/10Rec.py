
i = 1

def displayR(iNo):
    global i
    if(i<=iNo):
        print(i)
        i +=1
        displayR(iNo)

def main():
    iValue = int(input("Enter the value: "))
    displayR(iValue)

if __name__ == "__main__":
    main()