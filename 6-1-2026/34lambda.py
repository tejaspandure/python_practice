

def add():
    y = 10
    return (lambda x: x + y)

def main():

    iRet = add()
    print(iRet(10))

if __name__ == "__main__":
    main()