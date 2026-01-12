
import os

def main():

    print("Enter the file name that you want to open")
    Fname = input()

    if os.path.exists(Fname):
        fobj=open(Fname,'r')
        print("File open successfully")
        print(fobj)
        
    else:
        print("file not found")
if __name__ == "__main__":
    main()