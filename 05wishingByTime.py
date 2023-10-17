'''
# Morning time zone starts at 04:00:00 to 11:59:59
# Afternoon time zone starts at 12:00:00 to 15:59:59
# Evening time zone starts at 16:00:00 to 19:59:59
# Night time zone starts at 20:00:00 to 24:59:59
'''

name = input("Enter your name: ").title()
print(name)

from datetime import datetime

c_time = datetime.now()
cus_time = c_time.strftime("%H:%M:%S")

print(c_time)
print(cus_time)

hour = int(c_time.strftime("%H"))
print(hour)

minute = int(c_time.strftime("%M"))
print(minute)

sec = int(c_time.strftime("%S"))
print(sec)

if hour>=4 and hour<12:
    print("Good Morning")

elif hour>= 12 and hour<15:
    if hour == 12 and minute ==00:
        print("Good Noon")
    else:
        print("Good AfterNoon")

elif hour>=16 and hour<20:
    print("Good Evening")

else:
    print("GOod NIght")


'''
Method 02
'''

import time
t = time.strftime("%H:%M:%S")
print(t)

h = int(time.strftime("%H"))

m = int(time.strftime("%M"))

s = int(time.strftime("%S"))


if h>=4 and h<12:
    print("Good Morning")

elif h>= 12 and h<15:
    if h == 12 and m ==00:
        print("Good Noon")
    else:
        print("Good AfterNoon")

elif h>=16 and h<20:
    print("Good Evening")

else:
    print("GOod NIght")


'''
take time inpur from user and wish user
'''
from datetime import time

h = int(input())
m = int(input())
s = int(input())

timee = time(h, m, s)

print(timee)

if h>=4 and h<12:
    print("Good Morning")

elif h>= 12 and h<15:
    if h == 12 and m ==00:
        print("Good Noon")
    else:
        print("Good AfterNoon")

elif h>=16 and h<20:
    print("Good Evening")

else:
    print("GOod NIght")