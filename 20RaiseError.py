'''we learnt about the raising custom errors using raise keyword. Sometimes, we want to impose hard and fast 
regulations so, we can use customer errors if something violates those regulations so, that it does not create any 
problem later in the program execution and that error can be handled at that point of time only. 

In the previous Lecture, we learnt about how to handle errors using exception handling with try, except and finally 
blocks. We can also make our custom error classes using any base case error with our defined set of rules to raise 
that error whenever it violates those rules. '''


'''Here we are writing a poblem where the porgram accept just "quite" string and print it or the values between 
18 to 50. except those all input show value error'''

inpt = input("Enter an integer(between 5 and 9) : ")

try:
    if inpt == "quite":
        print("no error")

    elif 5 <= int(inpt) <= 9:
        print(f"{inpt}")

    elif int(inpt) < 5 or int(inpt) > 9:
        raise ValueError("Enter correct value to enter")
except ValueError as v:
    print(v)

'''Now writing a function like above'''


def run():
    a = input("Enter an integer(between 5 and 9) : ")

    try:
        if a == "quite":
            print("no error")

        elif 5 <= int(a) <= 9:
            print(f"{a}")

        elif int(a) < 5 or int(a) > 9:
            raise ValueError("Enter correct value to enter")
    except ValueError as v:
        print(v)


user_input = run()




