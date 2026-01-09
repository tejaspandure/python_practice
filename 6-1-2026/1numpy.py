import numpy as np

stu_roll = np.array([11,21,51,101])

#stu_roll = np.array([11,21,51,101],int)
#stu_roll = np.array([22.1, 33.3, 534.4, 343.3],float)
#ch_roll = np.array(['a','b','c','d'])
#name = np.array(['Rahul','Sonam','Raj'],dtype= str)

print(stu_roll[1])

stu_roll[1] = 14

print(stu_roll[1])



name = np.array([11,21,51,101,1001])
print(name)

print(name.dtype)
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
