from abc import ABC, abstractmethod

class Base(ABC):

    @abstractmethod
    def disp(self):
        pass

    def show(self):
        pass

class Derived(Base):
    def disp(self):
        print("Inside base class ")
        print("defining abstract method")

def main():

    dobj = Derived()

    dobj.disp()


if __name__ == "__main__":
    main()