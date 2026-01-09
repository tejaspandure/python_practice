#method overriding

class Number: 
    def Addition(self, iNo1, iNo2):
        print("Addition is : ",iNo1 + iNo2)

    def Multiplication(self, iNo1, iNo2):
        print("Multiplication is: ",iNo1 * iNo2)

def main():
    nobj = Number()
    nobj.Addition(19,22)
    nobj.Multiplication(33,22)

if __name__ == "__main__":
    main()