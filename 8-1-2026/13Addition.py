class Addition:
    def add(self, x, y):
        return x+y


def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    obj = Addition()
    iRet = obj.add(a, b)
    print("Addition is: ",iRet)


if __name__ == "__main__":
    main()
