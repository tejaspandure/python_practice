#linespace()

import numpy as np

#array_name = np.linespace(start,stop,num=50, endpoint = True)
#roll = np.linespace(1,8)
#roll = np.linespace(1,8,num=5)
#roll = np.linespace(1,8,5)

roll = np.linspace(1,11,5,endpoint=False)
n = len(roll)

i = 0

for i in range(n):
    print(roll[i])



for i in roll:
    print(i)


while(i<n):
    print(roll[i])
    i+=1

    