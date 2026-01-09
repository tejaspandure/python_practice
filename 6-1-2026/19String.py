
name = "Jay Ganesh"

print(name.upper())
print(name.lower())
print(name.swapcase())
print(name.title())

city = "sangamner" 
print(city.isupper())
print(city.islower())
print(city.istitle())

iMarks = "23458329324"

print(iMarks.isdigit())
print(iMarks.isalpha())
print(iMarks.isalnum())

space = "   "
print(space.isspace())

sSpace = "  asd lfj  "
print(sSpace.lstrip())
print(sSpace.rstrip())
print(sSpace.strip())

sName = "Jay GANESH"

print(sName.replace("GANESH","SHAM"))
print(sName.split(' '))

ssName = ('hello',"how",'are','you')
print('_'.join(ssName))

nName = "Hi How Are You"
print(nName.startswith('abc'))
print(nName.endswith('You'))