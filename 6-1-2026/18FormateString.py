str = "My age is {}"
print(str.format(62))

print("My age is: {}".format(62))

print("{} {}".format(10,20))
print("Mobile Price{}k, Computer price{}k".format(10,20))

print("{0}{1}".format(45,43))

print("{num1}".format(num1=10))

print("{num1}\t{num2}".format(num1=22,num2=44))


print("{num:05d}".format(num=43))
print("{num:+5d}".format(num=15))
print("{num:*<5d}".format(num=25))
print("{num:>5d}".format(num=33))
print("{num:*^10d}".format(num=33))

sName = "Rahul"
iAge = 55
fMarks = 55454.3445

print("My name is {} and my age is {}. I got {:.2} Percentage".format(sName,iAge,fMarks))


value=(10,20)
print("{0[0]} {0[1]}".format(value))

data1 = {'rahul':3999 , 'sonam':3433}
print("{0[rahul]:d}{0[sonam]:d}".format(data1))
print("{d[rahul]:d}{d[sonam]:d}".format(d=data1))

print("{rahul}{sonam}".format(**data1))