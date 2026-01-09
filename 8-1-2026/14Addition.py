class Addition:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y


def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    obj = Addition(a, b)
    iRet = obj.add()
    print("Addition is:", iRet)


if __name__ == "__main__":
    main()
