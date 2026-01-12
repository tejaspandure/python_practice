import os


def main():
    print("Enter the name of file that you want to open for reading")
    fName = input()

    if os.path.exists(fName):
        fobj = open(fName, 'r')
        print("successfully open in read mode")

        Data = fobj.read()
        print(Data)

        fobj.close()
        print("file gets closed successsfully")
    else:
        print("unable to open file as file is not present")

if __name__ == "__main__":
    main()