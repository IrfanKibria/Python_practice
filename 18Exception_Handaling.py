'''error handling is a way to hide our error and contiue the program. if there is a error in 
our program then full program will stop. here is a solution that is we have to detect the area where can get error 
and then we use "try except" function. that will skip the error and run the following code'''



'''Here we are makeing a problem of multiplication table and with some print function below. now if we input
string in user input it will give error. Now we are using try except function that will print the error in output and
run print functions below'''



a = input("Enter a number for tables: ")
print(f"The multiplication of {a} is: ")

try:
    for i in range(1, 11):
        if(i == 5) or (i==7):
            print("I want to gap in these feild for some reason")
            continue
        print(f"{int(a)} X {i} = {int(a) * i}")
except Exception as e:
    print(e)



'''WE  can also give a personal message for the error'''
a = input("Enter a number for table: ")

print(f"The multiplication of {a} is: ")

try:
    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a) * i}")
except:
    print("Please Input the valid Number")


print("here are some code")


'''We can handle value error'''

try:
    a = int(input("enter a number: "))

except ValueError:
    print("Enter a integer number")



'''we can use multiple exceptions'''

try:
    l = [2,4,6,7,8]
    i = int(input("Enter a index number of that list: "))
    print(l[i])

except ValueError as v:
    print(v)
    print('Invalid Input, Enter a integer Number')
except IndexError as I:
    print(I)
    print("Input valid Index Number")
