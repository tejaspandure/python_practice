#Hirerchichal inheritance

class Base:
    iX = 0
    iY = 0

    @classmethod
    def classMethods(cv):
        print("iX of Base : ",cv.iX)
        print("iY of base : ",cv.iY)

    def __init__(self):
        print("Base constructor: ")

    def fun(self):
        print("Inside base fun")

class Derived(Base):
    iA = 0
    iB = 0

    @classmethod
    def DerivedMethods(cv):
        print("iX of derived: ",cv.iA)
        print("iY of derived: ",cv.iY)
        
    def __init__(self):
        super().__init__()
        print("Derived consturcotr: ")

    def gun(self):
        print("Inside Derived Gun")

class DerivedX(Base):
    iP = 0
    iQ = 0

    @classmethod
    def DerivedXMethods(cv):
        print("iP of DerivedX: ",cv.iP)
        print("iQ of DerivedX", cv.iQ)

    def __init__(self):
        super().__init__()
        print("Derivedx constuructor")

    def run(self):
        print("Inside DerivedX run")


def main():
    dobj = Derived()
    dobj.fun()
    dobj.gun()

    ddobj = DerivedX()
    ddobj.fun()
    ddobj.run()

    ddobj.classMethods()
    dobj.DerivedMethods()
    ddobj.DerivedXMethods()


if __name__ == "__main__":
    main()