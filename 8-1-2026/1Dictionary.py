dNames = {101: "rahul",
         102: "sham",
         103: "ram",
         104: "aniket",
         105: "akshay"}

print("original dict: ",dNames)
print()
print("dictionary items",dNames.items())
print(type(dNames.items()))
print()
dList = dNames.items()
dListX = list(dList)
print(dListX)
print(type(dListX))

print()

for iCnt in dListX:
    for jCnt in iCnt:
        print(jCnt)


dKeys = dNames.keys()
print("Keys are : ",dKeys)
print("type",type(dKeys))

dvalues = dNames.values()
print("values are: ",dvalues)
print("type: ",type(dvalues))
print()

keys_list = list(dKeys)
print("listj of keys: ",keys_list)
print()

keys_values = list(dvalues)
print("list of values: ",keys_values)
print()

print(keys_list[0])
print(keys_list[1])

print()

print(keys_values[0])
print(keys_values[1])