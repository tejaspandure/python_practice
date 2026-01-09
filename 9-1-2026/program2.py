
class Number:
    iNo1 = 0
    iNo2 = 0

    @classmethod
    def classvariables(cv):
        print("iNo1 ",cv.iNo1)
        print("iNo2 ",cv.iNo2)

    def __init__(self,iA,iB):
        self.iNo1 = iA
        self.iNo2 = iB

    def Addition(self):
        return self.iNo1 + self.iNo2
    
    def Substraction(self):
        return self.iNo1 - self.iNo2
    
    def Multiplication(self):
        return self.iNo1 * self.iNo2
    
    def Division(self):
        return self.iNo1 / self.iNo2
    
    @staticmethod
    def Menu():
        print("Enter 1 for addition")
        print("Enter 2 for substraction")
        print("Enter 3 for multiplication")
        print("Enter 4 for division")
    


def  main():

    iValue1 = int(input("Enter the first number: "))
    iValue2 = int(input("Enter the second number: "))

    nobj = Number(iValue1,iValue2)

    nobj.Menu()

    iChoice = int(input("Enter the value: "))
    
    match iChoice:
        case 1:
            print("Addition of two number is: ",nobj.Addition())

        case 2:
            print("Substraction of two number is: ",nobj.Substraction())

        case 3:
            print("Multiplication of two number is: ",nobj.Multiplication())

        case 4: 
            print("Division of two number is: ",nobj.Division())

        case _:
            print("Invalid choice")

    nobj.classvariables()


if __name__ == "__main__":
    main()