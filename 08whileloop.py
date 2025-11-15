B = int(input("Enter a number"))
while(B>0):
    print(B)
    B = B-1



while True:
    
    input_year = int(input("Enter a year: "))
    if input_year % 4 == 0 and (input_year % 100 != 0 or input_year % 400 == 0):
        print(f"{input_year} is a leap year.")
        break
    else:
        print(f"{input_year} is not a leap year. Please try again.")
        continue