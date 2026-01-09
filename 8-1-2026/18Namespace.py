class Mobile:
    fp = 'Yes'

    @classmethod
    def is_fp(cls):
        print("finger print:",cls.fp)


realme = Mobile()
redmi = Mobile()
geek = Mobile()

print("class fp: ",Mobile.fp)
print("Realme : ",realme.fp)
print("redmi",redmi.fp)
print("geek",geek.fp)


print()

Mobile.fp = 'No'
print("Class fp: ",Mobile.fp)
print("realme: ",realme.fp)
print("redmi: ",redmi.fp)
print("geek: ",geek.fp)

print()

realme.fp= " Not working"
print("Class fp: ",Mobile.fp)
print("realme: ",realme.fp)
print("redmi: ",redmi.fp)
print("geek: ",geek.fp)