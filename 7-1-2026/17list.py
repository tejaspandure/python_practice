a = [10,20,-50,334.3,'tejas']

for iCnt in a:
    print(iCnt)

a[4] = 78

for iCnt in a:
    print(iCnt)


print("for loop")
iLen = len(a)

for iCnt in range(iLen):
    print(a[iCnt])


print("while loop")
iLen = len(a)
iCnt = 0

while(iCnt<iLen):
    print(a[iCnt])
    iCnt+=1