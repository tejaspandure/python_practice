
def show(list):
    print(list)
    print(type(list))

    for iCnt in list:
        print(iCnt)

    return list

def main():
    list = [10,20,39,'SPARTAN']
    iRet = show(list)

    print("new list: ,",iRet)

if __name__ == "__main__":
    main()