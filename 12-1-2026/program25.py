

import os


def main():
    print("Enter the folder name that you want to open: ")
    dName = input()

    print("list of files in directory are: ")

    if os.path.isdir(dName):
        for foldername, subfoldername, filenames in os.walk(dName):
            for fName in filenames:
                print(fName)
    else:
        print("No such directory")



if __name__ == "__main__":
    main()