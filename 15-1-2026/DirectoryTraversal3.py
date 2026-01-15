import sys
import os

def DirectoryWatcher(DirName):

    flag = os.path.isabs(DirName)
    
    if(flag ==False):
        DirName = os.path.abspath(DirName)

    exist = os.path.isdir(DirName)

    print("file names are : ")
    if (exist == True):
        for foldername, subfoldername, filename in os.walk(DirName):
            for fName in filename:
                print(fName)

    else:
        print("There is no such directory")

            

def main():
    print("Directory watcher")

    if(len(sys.argv)==2):

        if(sys.argv[1] =="--h" or sys.argv[1]=="--H"):
            print("this is directory use for searching ")
            print("\n")
            exit()

        if(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("usage of script : ")
            print("name_of_file  Name_of_directory")
            print("\n")
            exit()

        try:
            DirectoryWatcher(sys.argv[1])
            print("\n")
        except Exception as obj1:
            print("unable to perform the task due to exception : ",obj1)
            print("\n")



    else:
        print("invalid option")
        print("use --u for usage and --h for help")
        print()
        exit()

if __name__ == "__main__":
    main()