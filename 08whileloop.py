a = int(input())
while(a<=38):
    print(a)
else:
    print(f"{a} is Greater than 38")



while True:
    
    input_year = int(input("Enter a year: "))
    if input_year % 4 == 0 and (input_year % 100 != 0 or input_year % 400 == 0):
        print(f"{input_year} is a leap year.")
        break
    else:
        print(f"{input_year} is not a leap year. Please try again.")
        continue