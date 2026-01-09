

dict1 = {}
for iCnt in range(10):
    dict1[iCnt] = iCnt * 2

print("dict1",dict1)


dict1 = {  iCnt: iCnt * 2 for iCnt in range(10) }


dict1 = {}
for iCnt in range(10):
    if iCnt % 2 == 0:
        dict1[iCnt] = iCnt
    else:
        dict1[iCnt] = "Invalid"
print(dict1)


dict1 = { iCnt : (iCnt if iCnt % 2 == 0 else "invalid") for iCnt in range(10)}
print(dict1)


list = [(101,"Rahul"),(102,"Raj")]

dict1 = {k:v for k,v in list}
print(dict1)