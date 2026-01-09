#multiple

class Derived:
    iX = 0
    iY= 0

    @classmethod
    def DerivedMethods(cv):
        print("iX Derived: ",cv.iX)
        print("iY Derived: ",cv.iY)
        print()


    def __init__(self):
        print("Inside derived constructor")
        print()

    def Fun(self):
        print("Inside derived fun")
        print()

class DerivedX:
    iA = 0
    iB = 0

    @classmethod
    def DerivedXMethods(cv):
        print("iA of derivedX : ",cv.iA)
        print("iB of derivedX : ",cv.iB)
        print()

    def __init__(self):
        print("Inside derivedX constructor")
        print()

    def Gun(self):
        print("Inside DerivedX gun")
        print()

class Base(Derived,DerivedX):
    iP = 0
    iQ = 0

    @classmethod
    def BaseMethods(cv):
        
        print("iP of base: ",cv.iP)
        print("iQ of base: ",cv.iQ)
        print()

    def __init__(self):
        print("Derived Constructor")
        Derived.__init__(self)
        print()
        print("DerivedX Constructor")
        DerivedX.__init__(self)
        print()
        print("Inside Base constructor")
        print()

    def Run(self):
        print("inside base Run")
        print()


def main():
    bobj = Base()
    bobj.Run()
    bobj.Fun()
    bobj.Gun()

    print("___class methods___")
    bobj.BaseMethods()
    bobj.DerivedMethods()
    bobj.DerivedXMethods()



if __name__ == "__main__":
    main()