from threading import Thread
import threading
import time

class Demo(Thread):

    def run(self):
        sName = threading.current_thread().name
        print(sName)
        for iCnt in range(10):
            print(f"Running thread: {sName} with value: {iCnt}")
            Thread.sleep(4)
            


def main():
    dobj1 = Demo()
    dobj1.start()


if __name__ == "__main__":
    main()
