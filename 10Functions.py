'''A function is a block of code that performs a specific task then it is called'''

'''calculate avg beween two number by function'''

def CalculateAvg(a, b):
    c_avg = (a+b)/2
    print(c_avg)


x = int(input("Enter First Number: "))
y = int(input("Enter First Number: "))
CalculateAvg(x, y)


'''FInd max number between two number by function'''


def FindMax(a, b):
    if(a>b):
        print("first number is greater")

    else:
        print("second number is greater")


char1 = int(input("Enter First Number: "))
char2 = int(input("Enter First Number: "))
FindMax(char1, char2)


a = 8
b = 10
FindMax(a, b)


'''find avarage of numbers. we use return for if we want to store the result in a variable then we 
have to use return funtion. return use for that function have to retun someting when the function is called.
we use * for the arguments get into a tupple. and use ** for dict'''

def avg(*numbers):
    sum = 0
    print(type(numbers))
    for char in numbers:
        sum = sum +char
    return sum/len(numbers)
    # print(f"Avarage is {sum/len(numbers)}")


c = avg(6,5,3,6,3,5,7,100)
print(c)