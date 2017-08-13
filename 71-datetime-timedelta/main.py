import datetime

date_now = datetime.datetime.now()
print("Current Date:", str(date_now), "\n")

time_passed = datetime.timedelta(days=14, hours=2, minutes=24, seconds=33)
print("Time that will pass:", str(time_passed), "\n")

# Timedeltas can be added or subtracted to datetimes
date_then = date_now + time_passed
print("Date after time passing:", str(date_then), "\n")

# Timedeltas can be multiplied or divided
half_time_passed = time_passed / 2
date_midway = date_now + half_time_passed
print("Halfway date between these points:", str(date_midway))