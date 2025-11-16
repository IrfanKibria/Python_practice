'''
Beginner level

1. Print numbers from 1 to 100.
2. Print all even numbers between 1 and 50.
3. Print all odd numbers between 1 and 200.
4. Calculate the sum of numbers from 1 to N.
5. Print the multiplication table of any number.
6. Count vowels in a given string.
7. Find the largest number in a list using loops.
8. Reverse a string using a loop (no slicing).
9. Print a pattern: * ** *** **** *****
10. Calculate factorial of a given number using a loop.

'''

# 1. Print numbers from 1 to 100.

a = 1
while a<=100:
    print(a, end=" , ")
    a = a+1
print()



# Take user input as end range and print the numbers
end = int(input("Enter end range number: "))
b = 1
while(b<=end):
    print(b)
    b = b+1

# Take range from user and print Numbers

start = int(input("Enter start Range: "))
end = int(input("Enter end range: "))

while(start<=end):
    print(start)
    start += 1 



start = int(input("Enter start Range: "))
end = int(input("Enter end range: "))

for i in range(start, end):
    print(i)





"""Check Prime Number"""

p = int(input("Enter a Number for check Prime: "))

if p>1:
    for i in range(2, int(p**0.5)+1):
        if p%i==0:
            print(f"{p} is not a prime number")
        
    else:
        print(f"{p} is a prime number")



start = int(input("Enter a start number: "))
end = int(input("Enter a End number: "))

for n in range(start, end + 1):
    if n>1:
        for i in range(2, int(n**0.5)+1):
            if n%i==0:
                break
        
        else:
            print(f"{n} is prime number", end = ' , ')