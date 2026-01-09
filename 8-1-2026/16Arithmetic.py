
class Number:
    iNo1= 0 #class variables
    iNo2= 0

    def __init__(self,iX,iY):
        print("Constructor called")
        self.iNo1 = iX  #instance variable
        self.iNo2= iY
    
    def Addition(self):
        print("Addition function called")
        return self.iNo1 + self.iNo2
    
    def Substraction(self):
        print("Substraction function called")
        return self.iNo1 - self.iNo2
    
    def Multiplication(self):
        print("Multiplication function called")
        return self.iNo1 * self.iNo2
    
    def Division(self):
        print("Division function called")
        return self.iNo1 / self.iNo2


def main():
    iValue1 = int(input("Enter the value: "))
    iValue2 = int(input("Enter the second value: "))
    nobj = Number(iValue1,iValue2)

    print("1: Addition")
    print("2: Substraction")
    print("3: Multiplication")
    print("4: Division")


    iChoice = int(input("Enter your choice: "))

    match iChoice:
        case 1:
            print("Addition of given number is: ", nobj.Addition())

        case 2:
            print("Substraction of given number is: ",nobj.Substraction())

        case 3:
            print("Multiplication of the given number is : ",nobj.Multiplication())

        case 4:
            print("Division of given number is: ",nobj.Division())
    
        case _:
            print("Invalid choice")

if __name__ == "__main__":
    main()