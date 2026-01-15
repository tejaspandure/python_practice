import sys
import os

# Directory watcher

def DirectoryWatcher(Dirname):
    exist = os.path.isdir(Dirname)

    if exist:
        for foldername,subfoldername,filename in os.walk(Dirname):
            for fName in filename:
                print(fName)

    else:
        print("there is no such directory")

def main():
    print("--------------------------------------")
    print("----------Directory watcher-----------")
    print("---------------------------------------")

    if(len(sys.argv)==2):  #1 = filename #2 = --h/u

        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This directory is use for searching ")
            print("\n")
            exit()

        if(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Usage of script: ")
            print("Name_of_file Name_of_directory")

        try:
            DirectoryWatcher(sys.argv[1])
            print("\n")
        
        except Exception as obj2:
            print("unable to perform the task due to",obj2)
            print("\n")

    else:
        print("Invalid options: ")
        print("use --h for help and --u for usage")




if __name__ == "__main__":
    main()