
#nested class


class Army:

    def __init__(self):
        self.name = 'Rahul'
        self.gobj = self.Gun()   #Creating inner class object

    def show(self):
        print("Name : ",self.name)

    class Gun:
        def __init__(self):
            self.name = 'AK47'
            self.capacity = '75 rounds'
            self.length = '34.4 In'


        def disp(self):
            print("Name of gun: ",self.name)
            print("capacity; ",self.capacity)
            print("length : ",self.length)

def main():
    aobj = Army()
    print(aobj.name)
    print(aobj.show())
    print()
    print(aobj.gobj.name)
    print(aobj.gobj.capacity)
    print(aobj.gobj.length)
    print()
    g = Army().Gun()
    print(g.name)
    print(g.capacity)
    print(g.length)
    print()


if __name__ == "__main__":
    main()