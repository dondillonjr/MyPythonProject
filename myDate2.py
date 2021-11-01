from datetime import datetime
from datetime import date

#gets todays date with time
print(datetime.now())
#get current year
print(datetime.now().year)
#get current month
print(datetime.now().month)
#get current day
print(datetime.now().day)
#gets today date
print(date.today())
#gets the current time
print(datetime.now().time())
print()
now = datetime.now()
print(now)
print()
print(now.strftime("%m-%d-%Y %H:%M:%S"))
print()
print(now.strftime("%B-%d-%Y %H:%M:%S"))
print()
print(now.strftime("%b -%d-%Y %H:%M:%S"))