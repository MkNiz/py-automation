import datetime

# Store the current time
current = datetime.datetime.now()
print("Date:")
print(str(current.month) + "/" + str(current.day) + "/" + str(current.year) + "\n")

# Store a specified date and time
d = datetime.datetime(2000, 1, 1)
print("A Set Date:")
print("{0}/{1}/{2} {3}:{4}\n".format(str(d.month), str(d.day), str(d.year), str(d.hour), str(d.minute)))

# Get a datetime from an epoch timestamp

d2 = datetime.datetime.fromtimestamp(999999999)
print("A Date Converted from Epoch Time:")
print("{0}/{1}/{2} {3}:{4}\n".format(str(d2.month), str(d2.day), str(d2.year), str(d2.hour), str(d2.minute)))

# Datetimes can be compared
print("Is d greater than d2:", str(d > d2))