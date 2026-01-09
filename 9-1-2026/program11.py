#method overloading

class Number:

    def sum( iNo1 = None, iNo2 = None, iNo3 = None):
        if iNo1!=None and iNo2!=0 and iNo3 !=None:
            iResult = iNo1 + iNo2 + iNo3

        elif iNo1!=None and iNo2 !=None:
            iResult = iNo1 + iNo2
        
        else:
            iResult = "Please provide at least tow numbers"

        return iResult
        


def main():
    nobj= Number
    print(nobj.sum(10,11,39))



if __name__ == "__main__":
    main()