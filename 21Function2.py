# Write a recursion function which will return factorial of a number 
def f(n):
    if n == 0:
        return 1
    return n* f(n - 1)

print(f(8))




# Write a function which will find a numbers factorial
def find_fac():
    a = int(input("Enter a Number for find factotial: "))
    total = 1
    for i in range(1,a+1):
        total *= i
    print(total)
    return total
find_fac()



# Write a function which will find a list elements factorial
def find_listfac():
    a = list(map(int, input("Enter List elements: ").split()))
    fac_a = []
    for i in a:
        fact =1
        for j in range(1, i+1):
            fact *= j
        fac_a.append(fact)
    print(fac_a)
    return fac_a

find_listfac()
print(find_listfac())




# Write a function which will give exponent of a list elements
def find_expo():
    a = list(map(int, input("Enter the list: ").split()))
    expo_a = []
    exponent =1
    for i in a:
        exponent = i**2
        expo_a.append(exponent)
    return expo_a
print(find_expo())



# Write a program which will return 3 integers avarage
def num_avg(a,b,c):
    sum = a+b+c
    avg = sum/3
    return avg
print(num_avg(2,2,2))


# Write a Function which will return a list elements avarage
def list_avg():
    a = list(map(float, input("Enter numbers in the list: ").split()))
    div = len(a)
    avg = sum(a)/div
    return avg
print(list_avg())
