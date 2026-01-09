#inheritance
#single inheritance

class Base:
    iA = 0
    iB = 0

    def __init__(self):
        print("Base constructor: ")

    def Fun(self):
        print("Inside base fun")


class Derived(Base):
    iX = 0
    iY = 0

    def __init__(self):
        super().__init__() #call base constructor
        print("Derived constructor: ")

    def Gun(self):
        print("Inside derived gun")


def main():

    dobj = Derived()
    dobj.Fun()
    dobj.Gun()

if __name__ == "__main__":
    main()






