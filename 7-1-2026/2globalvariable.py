
a = 50

def show():
    x = 10 
    print("local variable",x)
    print("global variable: ",a)


def main():
    show()

if __name__ == "__main__":
    main()