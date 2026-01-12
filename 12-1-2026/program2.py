from abc import ABC, abstractmethod

class Demo(ABC):

    def iAddition(self, iA, iB):
        return iA + iB
    
    def iSubstraction(self, iA, iB):
        return iA - iB
    
    @abstractmethod
    def iMultiplication(self, iA, iB):
        pass


class Derived(Demo):

    def iDivision(self, iA, iB):
        return iA / iB
    
    def iMultiplication(self, iA, iB):
        return iA * iB


def main():

    dobj = Derived()

    iRet1 = dobj.iAddition(10, 11)
    print("Addition is:", iRet1)

    iRet2 = dobj.iSubstraction(22, 12)
    print("Subtraction is:", iRet2)

    iRet4 = dobj.iMultiplication(23, 5)
    print("Multiplication is:", iRet4)

    iRet3 = dobj.iDivision(50, 10)
    print("Division is:", iRet3)


if __name__ == "__main__":
    main()
