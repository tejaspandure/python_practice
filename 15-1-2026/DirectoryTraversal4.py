import os
import sys
import time

def DirectoryWatcher(DirName):
    
    flag = os.path.abspath(DirName)

    if(flag==False):
        DirName = os.path.abspath(DirName)

    exist = os.path.isdir(DirName)

    if(exist == True):
        for foldername,subfoldername,filename in os.walk(DirName):
            for fName in filename:
                print(fName)
    else:
        print("there is no such dirctory")

def main():
    print("Directory travseral script")


    if(len(sys.argv)==2):

        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This is directory watcher for searching file ")
            print("\n")

        if(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Usage of script")
            print("Name_OF_FILE  Name_OF_DIrectory")
            print("\n")

        try:
            starttime = time.time()
            DirectoryWatcher(sys.argv[1])
            endtime = time.time()
            print("time requird to excute the script is: ",endtime-starttime)
            exit()

        except Exception as obj2:
            print("Unable to perform script due to : ",obj2)
            print("\n")
            exit()

        
            


    else:
        print("invalid options")
        print("--u for usage and --h for help ")
        print("\n")
        exit()

if __name__ == "__main__":
    main()


#python DirectioryTravsersal4.py travsersal

#sys.argv[0]    DirectoryTravsersal4.py
#sys.argv[1]    travsersal

#len(sys.argv) = 2