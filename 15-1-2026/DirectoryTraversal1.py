import os

def main():
    print("Enter the name of directory that you want to search: ")
    dName = ()

    print("list of directory are: ")

    for foldername,subfoldername,filenames in os.walk(dName):
        for fname in filenames:
            print(fname)

if __name__ == "__main__":
    main()