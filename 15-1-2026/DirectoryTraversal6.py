import sys
import os
import time

def DirectoryWatcher(DirName):

    flag = os.path.isabs(DirName) #isabs: is absolute path

    if (flag == False):
        print("Path is not an absolute path")
        DirName = os.path.abspath(DirName)
        print("Converted absolute path is: ",DirName)

    exist = os.path.isdir(DirName)

    if(exist == True):
        for foldername, subfoldername, filename in os.walk(DirName):
            print("Currrent folder is: ",foldername)
            for name in filename:
                print("File name is: ",os.path.join(foldername,name))
    
    else:
        print("There is no such directory")

def main():
    print("------------------------------------------")
    print("------------Directory Watcher-------------")
    print("------------------------------------------")
    print("\n")

    if(len(sys.argv) == 2): #1 = file name 2 = --h/u

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This directory is use for searching the file")
            print("\n")
            exit()

        if(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Usage of the script: ")
            print("Name_of_file Name_of_Directory")
            print("\n")
            exit()

        try:
            starttime = time.time()
            DirectoryWatcher(sys.argv[1])
            endtime = time.time()
            print("Time required to execute the script is: ",endtime-starttime)
            print("\n")
            
        except Exception as obj2:
            print("Unable to perform the task due to ",obj2)
            print("\n")

    else:
        print("Invalid option")
        print("Use --h to get the help and use --u option to get the usage of application")
        print("\n")
        exit()
    
    print("------------------------------------------")
    print("------Thank you for using our script------")
    print("------------------------------------------")


if __name__ == "__main__":
    main()

# python DirectoryTravseral6.py traversal

#sys.argv[0]    DirectoryTravseral6.py
#sys.argv[1]    travsersal


#len(sys.argv) 2