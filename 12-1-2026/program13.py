#Creating a thread without using a class

from threading import Thread

def disp():
    for iCnt in range(5):
        print("child running")

tobj = Thread(target=disp)

tobj.start()

for iCnt in range(5):
    print("Main Thread")

for iCnt in range(10):
    print("Derived thread")


