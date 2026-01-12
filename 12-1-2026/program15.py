from threading import Thread
import threading

class Demo(Thread):

    def run(self):
        sName = threading.current_thread().name
        for iCnt in range(10):
            print(f"Running thread: {sName} with value: {iCnt}")


def main():
    dobj1 = Demo()
    dobj1.start()


if __name__ == "__main__":
    main()
