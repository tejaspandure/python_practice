from functools import reduce
a = [10,50,60,80,90,5,45,65]

result = list(filter(lambda n: (n>=60),a))
print(result)
print(type(result))

for i in result:
    print(i)


result = list(map(lambda n : n+1, a))
print(result)
print(type(result))


result = reduce( lambda x,y: x+y, a)
print(result)
print(type(result))