

def whileL(iNo):
    print("Inside while loop")
    i = 0
    while(i<iNo):
        print("Jay Ganesh")
        i +=1
    
def forL(iNo):
    i = 0

    for i in range(iNo):
        print("Jay Ganesh")
        i +=1




def main():

    print("Enter the frequency: ")
    iValue = int(input())
    whileL(iValue)
    forL(iValue)

if __name__ == "__main__":
    main()