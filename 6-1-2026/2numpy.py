import numpy as np

roll = np.array([11,21,51,101])


#for loop
print("---------for loop ---------------------")
print("Without index: ")
for i in roll:
    print(i)

print("with index")
n = len(roll)

for i in range(n):
    print('index', i, "=", roll[i])


#while loop

print("--------while loop --------------------")

n = len(roll)

i = 0

while(i<n):
    print(roll[i])
    i+=1



