

#import date time package 
#using this command pip install datetime
# this trick tell how many dats left in your birthday  by using python
# you should try it this is pretty awesome
#if you doubt about it i can help through comment box

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
    

