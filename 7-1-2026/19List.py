
def lList(a):
    lList = []

    for iCnt in range(a):
        lList.append(int(input()))

    return lList

def main():
    iValue = int(input("Entr teh frequency: "))
    iRet = lList(iValue)
    print(iRet)
    



if __name__ == "__main__":
    main()