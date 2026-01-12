from threading import Thread, current_thread

def disp():
    print("child thread object",current_thread())
    current_thread().name = 'Disp thread'
    print("new child thread object",current_thread().name)

t = Thread(target=disp)
t.start()

print("Main Thread",current_thread().name)
current_thread().name=("Docx Thread")
print("New main thread Name: ",current_thread().name)