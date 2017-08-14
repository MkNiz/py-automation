import datetime

date_str = "August 14, 2017"
date_dt = datetime.datetime.strptime(date_str, '%B %d, %Y')
print("Converted Date: " + str(date_dt))