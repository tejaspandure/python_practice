import os

def main():
    print("Enter the file name: ")
    fName = input()

    if os.path.exists(fName):
        fobj = open(fName,'r')
        print("file opens in reading mode successfully  ")

        # str1 = fobj.readline()
        # str2 = fobj.readline()
        # str3 = fobj.readline()

        # print(str1)
        # print(str2)
        # print(str3)
        # print("file reads successfully ")


        for iCnt in fobj:
            str = fobj.readlines()
            print(str)


        fobj.close()
        print("file close successfully")

    else:
        print("file not found")

    


if __name__ == "__main__":
    main()