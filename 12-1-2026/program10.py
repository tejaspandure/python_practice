

from datetime import date

dob = date(2004, 3, 10)

today = date.today()

iAge = today.year- dob.year - ((today.month, today.day) < (dob.month, dob.day))

print(iAge)
