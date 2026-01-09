#multilevel inheritance

class Base:
    iA = 0
    iB = 0

    def __init__(self):
        print("Inside the base constructor")

    def fun(self):
        print("Inside Base fun")


class Derived (Base):
    iX = 0
    iY = 0

    def __init__(self):
        super().__init__()
        print("Inside derived constructor")

    def gun(self):
        print("inside derived gun")


class DerivedX(Derived):
    iP = 0
    iQ = 0

    def __init__(self):
        super().__init__()
        print("Inside derivedX constructor")

    def run(self):
        print("Inside derivedX run")


def main():
    ddobj = DerivedX()
    ddobj.fun()
    ddobj.gun()
    ddobj.run()

if __name__ == "__main__":
    main()