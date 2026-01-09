nDict = {
            1: {'course':'java','fees':444444},
            2: {'course':'ppa','fees':30000},
            3: {'course': "lb", 'fees':78545}}

print("-----ID-----")
for id in nDict:
    print(id)

print("-----Keys-----")

for iCnt in nDict:
    for keys in nDict[iCnt]:
        
        print(keys,"=",nDict[iCnt][keys])   
print()


print("----dictionary----")

for iCnt in nDict:
    print(nDict[iCnt])

print()

print("-- for loop --")

for iCnt in nDict:
    if type(nDict[iCnt]) is dict:
        for jCnt in nDict[iCnt]:
            print(jCnt,'=',nDict[iCnt][jCnt])

    else:
        print(iCnt,"=",nDict[iCnt])

