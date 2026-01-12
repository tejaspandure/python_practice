import os

def main():
    print("Enter teh file that you want to create: ")
    Fname = input()

    open(Fname,'x')

if __name__ == "__main__":
    main()