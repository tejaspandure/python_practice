
import sys

def Addition(iA, iB):
    return iA+iB


def main():

    print("----------Automation to perfrom additon----------")

    if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
        print("this script is ued to perfrom addition")
        print()
        exit()

    if(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
        print("Usage of the script: ")
        print("Name_of_file First_argument second-argument")
        print("Note: Both the arguments should be in the integral formate")
        print()
        exit()
    
    else:
        print("Invalid option")
        print("use --h to get help and use --u for ussage")
        print()
        exit()

    iRet = Addition(int(sys.argv[1]), int(sys.argv[2]))
    print("Addition is: ",iRet)

if __name__ == "__main__":
    main()