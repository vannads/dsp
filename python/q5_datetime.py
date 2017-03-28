# Hint:  use Google to find python function

####a) 
from datetime import datetime

date_start = '01-02-2013'  
date_stop = '07-28-2015' 

date_format = "%m-%d-%Y"

d1 = datetime.strptime(date_start, date_format)
d2 = datetime.strptime(date_stop, date_format)
numOfDays = d2 - d1
print("Q5_a: Number of days = ",numOfDays.days)  

####b)  
date_start = '12312013'  
date_stop = '05282015' 

date_format = "%m%d%Y"

d1 = datetime.strptime(date_start, date_format)
d2 = datetime.strptime(date_stop, date_format)
numOfDays = d2 - d1
print("Q5_b: Number of days = ",numOfDays.days)  

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015' 

date_format = "%d-%b-%Y"

d1 = datetime.strptime(date_start, date_format)
d2 = datetime.strptime(date_stop, date_format)
numOfDays = d2 - d1
print("Q5_c: Number of days = ",numOfDays.days)
