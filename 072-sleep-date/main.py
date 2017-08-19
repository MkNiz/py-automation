import datetime, time

this_sep = datetime.datetime(2017, 9, 1)
print("This program will run the loop until September 1, 2017 arrives")
while datetime.datetime.now() < this_sep:
    print("It's not September 1 2017 yet.")
    time.sleep(1)
print("It's September 1 2017 or later.")