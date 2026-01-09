
lList = [11,21,51,101]
print("before inserting list: ",lList)

iIndex = lList.index(21)
print("Index of 21",iIndex)

print("Reverse list is: ",lList.reverse())

lList.insert(1,45)
print("After inserting element: ",lList)

lList.remove(21)
print("after removing 21",lList)

lList.pop()
print("After remove the last elemtent: ",lList)

lllList = [11,21,4,101]
llList  = [55,6,4,3,22]

lllList.extend(llList)
print("extended list: ",lllList)

print("occurance of 4",lllList.count(4))

lllList.sort()
print("sorted list: ",lllList)

iList = lllList[1:7:1]
print("sliced list: ",iList)


iiList = lllList + llList
print(iiList)


iResult = lllList * 4
print("repetition",iResult)