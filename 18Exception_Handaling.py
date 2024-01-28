'''error handling is a way to hide our error and contiue the program. if there is a error in 
our program then full program will stop. here is a solution that is we have to detect the area where can get error 
and then we use "try except" function. that will skip the error and run the following code'''



'''Here we are makeing a problem of multiplication table and with some print function below. now if we input
string in user input it will give error. Now we are using try except function that will print the error in output and
run print functions below'''



a = input("Enter a number for table: ")
print(f"The multiplication of {a} is: ")

for i in range(1, 11):
    print(f"{int(a)} X {i} = {int(a) * i}")