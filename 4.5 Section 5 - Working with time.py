from datetime import date, time

today = date.today()

print('Today', today)
print('Year:', today.year)
print('Month:', today.month)
print('Day:', today.day)

my_date = date(2003, 12, 29)
print(my_date, end = '\n\n')

import time

timestamp = time.time()
print('Timestamp:', timestamp) # gives no of seconds since jan 1 1970

d = date.fromtimestamp(timestamp) # use date's fromtimestamp to create a date object
print('Date:', d)

# replace()

d = date(1991, 2, 5)
print(d)

d = d.replace(1992, 1, 16)
print(d, end = '\n\n')

# weekday()

print(d.weekday()) # 0 is monday
print(d.isoweekday(), end = '\n\n') # 1 is monday

# time(hour, minute, second, microsecond, tzinfo, fold)

from datetime import time # time class

t = time(14, 53, 20, 1)

print("Time:", t)
print("Hour:", t.hour)
print("Minute:", t.minute)
print("Second:", t.second)
print("Microsecond:", t.microsecond, end = '\n\n')

# time module

import time

class Student:
    def take_nap(self, seconds):
        print('Very tired. Take a nap, see you later')
        time. sleep(seconds)
        print('Slept well, time to work!')

student = Student()
student.take_nap(0.1)
print(end = '\n\n')

# ctime() converts the time in seconds since Jan 1 1970

timestamp = 1500000000
print(time.ctime(timestamp), end = '\n\n')

# gmtime(), localtime()

# The difference between them is that
# the gmtime function returns the struct_time object in UTC,
# while the localtime function returns local time. For the gmtime

timestamp = 1572879180
print(time.gmtime(timestamp))
print(time.localtime(timestamp),  end = '\n\n')

# asctime() - converts gmtime output (struc_time object) into a string,
# mktime() - converts struc_time object into a unix epoch

timestamp = 1572879180
st = time.gmtime(timestamp)

print(time.asctime(st))
print(time.mktime((2019, 11, 4, 14, 53, 0, 0, 308, 0)),  end = '\n\n')

# several datetime methods returning current date and time
from datetime import datetime

print("today:", datetime.today())
print("now:", datetime.now())

dt = datetime(2020, 10, 4, 14, 55)
print('timestamp: ', dt.timestamp()) # timestamp
print(dt.strftime('%Y/%m/%d')) # formatting
print(dt.strftime("%Y/%B/%d %H:%M:%S"), end = '\n\n')

d1 = date(2020, 11, 4)
d2 = date(2019, 11, 4)

print(d1 - d2, end = '\n\n')

dt1 = datetime(2020, 11, 4, 0, 0, 0)
dt2 = datetime(2019, 11, 4, 14, 53, 0)

print(dt1 - dt2, end = '\n\n')

from datetime import timedelta

delta = timedelta(weeks=2, days=2, hours=3)
print("Days:", delta.days)
print("Seconds:", delta.seconds)
print("Microseconds:", delta.microseconds, end = '\n\n')

# Write a program that creates a datetime object for November 4, 2020 , 14:53:00.
# The object created should call the strftime method with the appropriate format to display the following result:

# Output
# 2020/11/04 14:53:00
# 20/November/04 14:53:00 PM
# Wed, 2020 Nov 04
# Wednesday, 2020 November 04
# Weekday: 3
# Day of the year: 309
# Week number of the year: 44

from datetime import datetime

my_date = datetime(2020, 11, 4, 14, 53)

print(my_date.strftime("%Y/%m/%d %H:%M:%S"))
print(my_date.strftime("%y/%B/%d %H:%M:%S %p"))
print(my_date.strftime("%a, %Y %b %d"))
print(my_date.strftime("%A, %Y %B %d"))
print(my_date.strftime("Weekday: %w"))
print(my_date.strftime("Day of the year: %j"))
print(my_date.strftime("Week number of the year: %W"))
