class Number:
    iX = 0
    iY = 0

    def __init__(self,iA,iB):
        self.iX = iA
        self.iY = iB

        

    def Substraction(self):
        return self.iX - self.iY
        
def main():
    
    iValue1 = int(input("Enter the value: "))
    iValue2 = int(input("Enter the second value: "))
    nobj = Number(iValue1,iValue2)
    iRet = nobj.Substraction()
    print("Substraction of teh given number is : ",iRet)

if __name__ == "__main__":
    main()