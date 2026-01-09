#Duck typing 

class Duck:
    def walk(self):
        print("duck walk")
        print("thapak thapak thapak thapak")

class Horse:
    def walk(self):
        print("Horse walk")
        print("tabdak tabdak")

class Cat:
    def talk(self):
        print("Cat voice")
        print("meow meow")


def Walk(obj):
    print("Walk function")
    obj.walk()
    
def Talk(obj):
    print("talk funciton")
    obj.talk()

dobj = Duck()
Walk(dobj)
hobj = Horse()
Walk(hobj)

cobj = Cat()
Talk(cobj)
