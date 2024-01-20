'''Recursion is a kind of function. we know A function can call other function. It is possible that A function can
call itself. These types of function is called recursive function'''


def fac_any_number(n):
    '''here we are making a function which can return any number of factorial which is take input from user'''
    if(n==0 or n==1):
        return 1
    else:
        return n * fac_any_number(n-1)


a = int(input("Enter a number: "))

result = fac_any_number(a)
print(f"The factorial of {a} is: {result}")



'''In this example we find fibonacchi sequence'''

def fibo(n):
    if(n <= 1):
        return n
    else:
        return fibo(n-1) + fibo(n-2)
    
a = int(input("enter a number which you want to find sequence: "))

res = fibo(a)
for i in range(a):
    print(fibo(i))



