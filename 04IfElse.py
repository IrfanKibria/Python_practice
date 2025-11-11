# '''Driving test problem. If Driver age is less than 18 or age more than 70 then they cannot dirive'''

# Age = int(input('Enter Your age: '))
# print("Input age is: ",Age)

# if Age>18 and Age<=70:
#     print("You can Drive")

# elif Age>70:
#     print("You can not Drive. Over Aged")

# else:
#     print("You can not Drive. Below aged")


# '''Write a program that takes an integer and prints whether it is even or odd.'''

# num_check = int(input("Enter a number for check it is even or odd: "))

# if num_check%2==0:
#     print(f"{num_check} this number is even")

# else:
#     print(f"{num_check} this number is odd")




# num_check = int(input("Enter a number for check it is even or odd: "))

# if num_check%2!=0:
#     print(f"{num_check} this number is ODD")

# else:
#     print(f"{num_check} this number is Even")




# '''Input a number and check if it’s positive, negative, or zero.'''

# num = int(input("Input a Number for check positive or negative or zero: "))

# if num>0:
#     print(f"{num} is positive")
# elif num<0: 
#     print(f"{num} is negative")
# elif num==0:
#     print(f"{num} is zero")

# '''Input two numbers and print which one is larger (or if they’re equal).'''
# num = int(input("Enter First Number: "))
# num2 = int(input("Enter Second Number: "))

# if num>num2:
#     print(f"{num} is greater")
# elif num2>num:
#     print(f"{num2} is greater")
# elif num == num2:
#     print(f"Both numbers are equal")

# '''Input a student’s marks and print their grade using these rules:80–100: A+, 70–79: A, 60–69: A−, 50–59: B
# Below 50: Fail
# '''

# result = int(input("Enter Student Number: "))

# if 100>=result>=80:
#     print("He got A+")
# elif 79>=result>=70:
#     print("He got A")
# elif 69>=result>=60:
#     print("He got A-")
# elif 59>=result>=50:
#     print("He got B")
# elif 50>result:
#     print("He Failed")
# else:
#     print("Enter a valid result")


# '''Input a year and check if it’s a leap year or not.'''

# leap = int(input("Enter a year for check leap year or not: "))

# if (leap%4==0 and leap%100!=100) or leap%400==0:
#     print(f"{leap} is leap year")
# else:
#     print("Not leap year")


# '''Input a letter and determine whether it is a vowel or consonant.'''

# char = input("Enter a character: ")
# if char in 'aeiou' or char in 'AEIOU':
#     print(f"{char} is vowel")
# else:
#     print(f"{char} is consonent")


'''Electricity Bill Calculator
Given units consumed, calculate total bill:
First 100 units → 5 taka/unit
Next 100 units → 8 taka/unit
Beyond 200 units → 12 taka/unit
'''

unit = int(input("Input units: "))
bill = 0
if unit<=100:
    bill = unit*5
elif unit<=200:
    bill = 100 * 5
    bill += (unit - 100)* 8
else:
    bill = 100 * 5
    bill += 100 * 8
    bill += (unit -200)*12

print(f"Total bill of {unit} is {bill}")



'''Triangle Type Checker
Input three sides of a triangle and determine if it’s:
Equilateral
Isosceles
Scalene
Or invalid (not a triangle)
'''


'''Salary Bonus
If employee’s years of service > 5, give a 10% bonus; otherwise, no bonus.
'''


'''Number Divisibility Test
Check whether a number is divisible by both 3 and 5, only 3, only 5, or neither.
'''

