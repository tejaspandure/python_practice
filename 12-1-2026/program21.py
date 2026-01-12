import os

def main():

    print("Enter the file that you want to delete")
    Fname = input()

    if os.path.exists(Fname):
        os.remove(Fname)
        print("The file is successfully removed")
    
    else:
        print("The file is not exists enter the name correctly")

if __name__ == "__main__":
    main()