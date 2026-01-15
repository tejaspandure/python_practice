
import sys

def Addition(iA, iB):
    return iA+iB


def main():

    print("----------Automation to perfrom additon----------")

    if(len(sys.argv)==2):

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
    
    if(len(sys.argv)==3):
        try:
            iRet = Addition(int(sys.argv[1]), int(sys.argv[2]))
            print("Addition is: ",iRet)
            print()
        
        except ValueError as obj1:
            print("invalid type of arguments")
            print()

        except Exception as obj2:
            print("Unable to perform the task due to ",obj2)
            print()
        
    else:
        print("invalid options")
        print("use -- h to get help and use --u for usage")
        print()
        exit()

    
    print("----------------------------------------------")
    print("----------Thank you for using our script----------")
    print("-------------------------------------------------")

    print()
    
if __name__ == "__main__":
    main()