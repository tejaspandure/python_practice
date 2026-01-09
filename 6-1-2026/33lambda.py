#nested lambda

def Add(ix,iY):
    iX = 10
    iZ = iX +iY
    return iZ

AddX = lambda iX = 10: (lambda iY: iX + iY)


# calling lambda function inside a function

def show(a):
    print(a(8))

ShowX = lambda iY : iX = 8

def main():
    iRet = AddX()
    iRetX = iRet(5)
    print(iRetX)

    iRetXX = ShowX()
    print(iRetXX)

    


if __name__ == "__main__":
    main()
