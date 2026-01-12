#Creating a thread without using a class

from threading import Thread

def disp(iA,iB):
    print("Thread running", iA,iB)

for iCnt in range(5):
    tobj = Thread(target=disp, args=(10, 20 ))


tobj.start()