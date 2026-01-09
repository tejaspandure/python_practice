
def Addition(*iNo):
    iAns = 0

    print(type(iNo))
    print(len(iNo))

    for i in iNo:
        iAns = iAns+i
    
    return iAns

    

def main():
    Result = 0
    Result = Addition(10,20,30,40)
    print("Addition is: ",Result)


if __name__ == "__main__":
    main()