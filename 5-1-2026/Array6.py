
from array import *

roll = array('i',[])
n = int(input("Enter the frequency: "))

for i in range(n):
    roll.append(int(input("Enter the elements: ")))

n = len(roll)
i = 0

for i in range(n):
    print(roll[i])
    i+=1


from array import *

roll = array('i',[])
n = int(input("Enter the frequency: "))

i = 0
j = 0
while(i<n):
    roll.append(int(input("Enter the elements: ")))
    i+=1


while(j<len(roll)):
    print(roll[j])
    j+=1