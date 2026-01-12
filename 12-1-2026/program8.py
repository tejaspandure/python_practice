from datetime import date, datetime

d1 = date(year=2019, month=6, day=4)
d2 = date(year=2026, month=5, day=23)

print(d1 == d2)
print(d1 > d2)
print(d1 < d2)


dt = datetime.today()
print(dt)
print()

newd1 = dt.strftime(" %B, %d, %Y" )
print(newd1)

newd2 = dt.strftime("%d/%b/%Y")
print(newd2)

newd3 = dt.strftime("%d-%m-%Y")
print(newd3)

newt = dt.strftime("%H : %M : %S")
print(newt)
