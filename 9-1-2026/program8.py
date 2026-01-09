
class Father: 
    def __init__(self,m,role):
        self.money= m
        self.role = role

        print("father constructor")

    def show(self):
        print("Father class ")

class child(Father):

    def __init__(self,m,job,role):
        super().__init__(m,role)
        self.job = job

    def disp(self):
        print("Money is: ",self.money)
        print("Your job role is: ",self.job)
        print("Your role is : ",self.role)


def main():
    sobj = child(10,'SDE','backend developer')
    sobj.disp()

if __name__ == "__main__":
    main()