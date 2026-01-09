def Addition(iA, iB):
    iAns = 0
    iAns = iA + iB
    return iAns

AdditionX = lambda iA, iB : iA + iB

def main():
    iRet = Addition(10,11)
    print("Addition is: ",iRet)

if __name__ == "__main__":
    main()