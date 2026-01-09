
class Number:
    iNo1= 0 #class variables
    iNo2= 0

    @classmethod
    def showClassValues(cls):
        print("@ClassMethod annotation gets called")
        print("Class variable: ")
        print("iNo1: ",cls.iNo1)
        print("iNo2: ",cls.iNo2)
        print()

    def __init__(self,iX,iY):
        print("Constructor called")
        self.iNo1 = iX  #instance variable
        self.iNo2= iY
        print()
    
    def Addition(self):
        print("Addition function called")
        print()
        return self.iNo1 + self.iNo2
    
    
    def Substraction(self):
        print("Substraction function called")
        print()
        return self.iNo1 - self.iNo2
    
    def Multiplication(self):
        print("Multiplication function called")
        print()
        return self.iNo1 * self.iNo2
    
    def Division(self):
        print("Division function called")
        print()
        return self.iNo1 / self.iNo2
    
    @staticmethod
    def Menu():
        print("@staticmethod annotation gets called")
        print("1: Addition")
        print("2: Substraction")
        print("3: Multiplication")
        print("4: Division")


def main():
    iValue1 = int(input("Enter the value: "))
    iValue2 = int(input("Enter the second value: "))
    print()
    nobj = Number(iValue1,iValue2)

    nobj.Menu()

    iChoice = int(input("Enter your choice: "))
    print()

    match iChoice:
        case 1:
            print("Addition of given number is: ", nobj.Addition())
            print()

        case 2:
            print("Substraction of given number is: ",nobj.Substraction())
            print()

        case 3:
            print("Multiplication of the given number is : ",nobj.Multiplication())
            print()

        case 4:
            print("Division of given number is: ",nobj.Division())
            print()
    
        case _:
            print("Invalid choice")
            print()

    nobj.showClassValues()

if __name__ == "__main__":
    main()