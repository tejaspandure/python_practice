#Set comprehension

set1 = {1,2,3,4,5}

set2 = set()

for iCnt in set1:
    set2.add(iCnt+1)

print(set2)
print(type(set2))


#with set comprehension

set2 = {3,4,5,6,3,4,2}
iResult  = {i+1 for i in set2}
print(iResult)
print(type(iResult))