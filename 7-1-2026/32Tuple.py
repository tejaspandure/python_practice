
Arr = (11,21,90,True,"Marvellous",11)

print(type(Arr))
print(len(Arr))
print(Arr[0])
print(Arr[2])


#Arr[0] = 21

for iCnt in Arr:
    print(iCnt)


n = len(Arr)

print("For loop")
for iCnt in range(len(Arr)):
    print(Arr[iCnt])

iCnt = 0
print("while loop")
while iCnt<(len(Arr)):
    print(Arr[iCnt])
    iCnt+=1


slice = Arr[1:4]
print("Slicing the tuple",slice)


Brr = (55,34,34)
tResult = Arr + Brr

print("Concatinated tuples : ",tResult)

tArr = (11,21,90,True,"Marvellous",11)
print("tArr",tArr)
tBrr = 101,203

slice1 = tArr[0:4]
print("sliced 1",slice1)

slice2 = tArr[4:]
print("sliced 2",slice2)

iResult = slice1 + tBrr + slice2
print("Result after slicing and adding new tuple : ",iResult)


delete1 = tArr[0:3]
delete2 = tArr[4:]

iResult = delete1 + delete2
print("deleting the value at 4 after : ",iResult)



iArr = []

iValue = int(input("Enter the no of elements: "))

for i in range(iValue):
    iArr.append(int(input("Enter the elements: ")))

print(type(iArr))

iArr = tuple(iArr)

print(iArr)
print(type(iArr))
print("tuple elemtns: ")
for iCnt in iArr:
    print(iCnt)