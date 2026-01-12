import os

def main():
    print("Enter the file that you want to craete: ")
    Fname = input()

    if os.path.exists(Fname):
        print("File is already present")
    else:
        open(Fname,'x')
        print("file is successfully created")

if __name__ == "__main__":
    main()
