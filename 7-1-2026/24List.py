

a = [[11,21,51,101],[33,55,33,55]]

n = len(a)

for i in range(n):

    for j in range(len(a[i])):

        print(i,j,a[i][j])
    print()


n = len(a)
i = 0

while(i<n):
    if type(a[i]) is list:
        if len(a[i]) > 1:
            j = 0
            m = len(a[i])

            while(j<m):
                print(i,j, a[i][j])
                j+=1
                
            i+=1

    else:
        print(i,a[i])
        i+=1
        