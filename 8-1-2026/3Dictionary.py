dNames = {101: "rahul",
         102: "sham",
         103: "ram",
         104: "aniket",
         105: "akshay"}

print("original dictionary: ",dNames)
print(type(dNames))
print()

setdefault = dNames.setdefault(105,'ram')
print("set default: ",setdefault)


print("______________for loop____________")

iCnt = 0

for iCnt in dNames:
    print("key: ",iCnt,"value: ",dNames[iCnt])

print("---------------Getting input from user-------------")

dA = {}

print("Enter the frequency: ")
iValue = int(input())

for iCnt in range(iValue):
    iX = int(input("Enter the key: "))
    iY = input("Enter the value: ")
    dA.update({iX:iY})

print(dA)
for iCnt in dA:
    print("Entered items are ",iCnt,dA[iCnt])
    