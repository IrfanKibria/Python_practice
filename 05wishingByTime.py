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


a =[2, 56, 156, 86, 2, 45]

b = min(a)

print(b)


