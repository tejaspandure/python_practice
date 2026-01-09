#variable length arguments: 

def add(x ,*num):
    iResult = x + num[0] +num[1]+ num[2]
    return iResult

def main():
    iRet=add(3, 4,5,6)
    print(iRet)

if __name__ == "__main__":
    main()