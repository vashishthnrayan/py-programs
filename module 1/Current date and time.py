# import datetime

# x = datetime.datetime.now()
# print("Current date and time:")

# print(x)

from datetime import date,time,datetime

today = date.today()
now = datetime.now()
print("Today's date: ", today)
print("\nCurrent date & time is : ", now)

print("\n Date components:", today.day, today.month, today.year)