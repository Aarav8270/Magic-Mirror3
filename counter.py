from bs4 import BeautifulSoup
from datetime import datetime

file = open("C:/Users/agupta-22/Magic-Mirror/counter.txt", "w")
weekday = datetime.today().strftime("%A")

time = datetime.now().strftime("%H:%M")
count= 124
if count == 0:
     count=365
if time == "24:00":
 count2=count-1
 count2 = str(count2)
 file.write(count2 +' Days Left!')
 count=count-1
elif time != "24:00":
 count2=count
 count2 = str(count2)
 file.write(count2 +'\nDays Left!')

 