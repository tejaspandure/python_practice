
import sys

def Addition(iA, iB):
    return iA+iB

def main():
    iRet = Addition(int(sys.argv[1]), int(sys.argv[2]))
    print("Addition is: ",iRet)

if __name__ == "__main__":
    main()