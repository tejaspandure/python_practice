
lst1 = [0,1,2,3,4,5,6,7,8,9,10]

new_lst1 = []

for iCnt in lst1:
    new_lst1.append(iCnt+1)

print(new_lst1)


#list comprehension

lst2 = [1,2,3,4,5,6,7,8,9,10]

rResult = [iCnt + 1 for iCnt in lst2]

print("list comprehension: ",rResult)

list3 = []

for iCnt in range(40):
    if iCnt % 2 == 0:
        list3.append(iCnt)
        
print(list3)
   

rReulst = [iCnt for iCnt in lst2 if iCnt%2==0]
print("list comprehension: ",rReulst)

list4 = [iCnt for iCnt in range(70) if iCnt%5==0]
print("list of %5",list4)


#list comprehension with if else statement

list5 = [iCnt if iCnt % 2 == 0 else " invalid" for iCnt in range(5)]
print("list5 ",list5)

list6 = []

for iCnt in range(10):
    if iCnt % 2 == 0:
        list6.append(iCnt)
    else:
        list6.append("invalid")
print(list6)

list6 = [iCnt if iCnt % 2 == 0 else "invalid" for iCnt in range(10)]
print("list6",list6)


#Nested list comprehension

for iCnt in range(6,8):
    for jCnt in range(4,7):
        pass

lst = [[iCnt*jCnt for jCnt in range(4,7)] for iCnt in range(6,8)]
print(lst)

