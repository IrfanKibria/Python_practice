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



# Take range from user and print Numbers(with for loop)

start = int(input("Enter start Range: "))
end = int(input("Enter end range: "))

for i in range(start, end+1):
    print(i)



# 2. Print all even numbers between 1 and 50.
ends= int(input("Enter end range: "))
start =1
lists= []
while(start<= ends):
    if start%2==0:
        print(f"{start} is even number")
        lists.append(start)
    start += 1
print()
print(lists)


# Take range from user and print even numbers and even numbers stored in list
start = int(input("enter start range: "))
end = int(input("enter end range: "))
evens = []
while(start<=end):
    if start%2==0:
        print(f"{start}", end = " ")
        evens.append(start)
    start += 1
print()
print(evens)


# Take range from user and print even numbers and even numbers stored in list(For Loop)

start = int(input("enter start range: "))
end = int(input("enter end range: "))
evens = []
odd = []
for i in range(start, end+1):
    if i%2==0:
        print(f"{i} is even number")
        evens.append(i)
    else:
        print(f"{i} is odd")
        odd.append(i)
print()
print(f"List of even number {evens}")
print(f"List of odd number {odd}")





# 4. Calculate the sum of numbers from 1 to N.

end = int(input("Enter the targeted end: "))
total = 0
start = 1
while(start<=end):
    total += start
    start +=1
print(total)
    

# Calculate the sum of numbers from 1 to N.(For Loop)

start = int(input("Enter the start range Number: "))
end = int(input("Enter the end range number: "))
total = 0
for i in range(start, end +1):
    total += start
    start += 1
print(total)




# 5. Print the multiplication table of any number.

a= int(input("Enter a number for Multiplication table: "))
i=1
while(i<=10):
    print(f"{a} * {i} = {a*i}")
    i+=1


# Print the multiplication table of any number.(For Loop)

a= int(input("ENter a Number for Multiplication table: "))

for i in range(1,11):
    print(f"{a} * {i} = {a*i}")




# 6. Count vowels in a given string.

a = input("Enter a string: ")
vowels = 'aeiouAEIOU'
count = 0
i = 0
while i < len(a):
    if a[i] in vowels:
        count += 1
    i +=1
print(f"total count of vowels: {count}")

# Count vowels in a given string.(for loop)

a = input("Enter a String: ")
count = 0

for i in a:
    if i in 'aeiouAEIOU':
        count += 1
print(f"Number of vowels: {count}")






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