#import date time package 
#this code is easy to understand
#this repository to learn you can find how many days left in your birthday  this very pretty awesome trick

import datetime
birth=datetime.date(2010,9,10)
print("Birtj",birth)
today=datetime.date.today()
print("Today",today)
if(today.month==birth.month and today.day>=birth.day or today.month>birth.month):
    nextbirthyear=today.year+1
else:
    nextbirthyear=today.year

nextbirth=datetime.date(nextbirthyear,birth.month,birth.day)
print("nextbirtday:",nextbirth)
diff=nextbirth-today
print(" day left for nextbirthday:",diff.days)
    

