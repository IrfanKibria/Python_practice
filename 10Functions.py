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