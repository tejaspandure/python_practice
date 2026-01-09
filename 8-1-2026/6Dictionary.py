
def show(d):

    for iCnt in d:
        print(iCnt,"=",d[iCnt])
    return d

def main():
    dict = {101:'Rahul',102:'RAj',103:'Sonam'}
    dRet = show(dict)
    print("returend dictionary: ",dRet)

if __name__ == "__main__":
    main()