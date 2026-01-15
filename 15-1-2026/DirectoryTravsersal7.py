import os
import sys
import time

def DirectoryWatcher(DirName):

    flag = os.path.isabs(DirName)

    if(flag==False):
        print("path is not absolute path")
        DirName = os.path.isabs(DirName)
        print("converted absolute path is: ",DirName)

    exist = os.path.isdir(DirName)

    if(exist == True):
        for foldername, subfoldername, filename in os.walk(DirName):
            for fName in filename:
                print("File name is: ",os.path.join(foldername,fName))
                print("file size is: ",os.path.getsize(foldername,fName))
                print()

    else:
        print("There is no such directory")

def main():
    print("------------------------------------------")
    print("------------Directory Watcher-------------")
    print("------------------------------------------")
    print("\n")

    if(len(sys.argv)==2):

        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("this script is for directiory travseral")
            print("\n")
            exit()

        if(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("usage of script : ")
            print("Name_of_file  Directory_name")
            print("\n")
            exit()

        try:
            starttime = time.time()
            DirectoryWatcher(sys.argv[1])
            endtime = time.time()
            print('total time is: ',endtime-starttime)
            print("\n")
        
        except Exception as obj1:
            print("Unable to pefrom the task due to : ",obj1)
            print("\n")

    
    else:
        print("unable to perfrom script: ")
        print("use --u for usage use --h for help")
        print("\n")
        exit()

    print("------------------------------------------")
    print("-------Thank you for using script--------")
    print("------------------------------------------")
    print("\n")

if __name__ == "__main__":
    main()