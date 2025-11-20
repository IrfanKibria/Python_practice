"""Intermediate Level Problems
1. Print Fibonacci series for N terms.
2. Check if a number is prime using loops.
3. Reverse an integer using a loop.
4. Count digits in a number.
5. Sum the digits of an integer.
6. Keep taking user input until 'exit' is typed.
7. Print all multiples of 3 between 1 and 300.
8. Remove duplicates from a list using loops.
9. Count how many times a value appears in a list.
10. Find the second largest number in a list using loops."""








# 2. Check if a number is prime using loops.


f = int(input("Enter a number to check Prime: "))

if f>1:
    for i in range(2, int(f**0.5)+1):
        if f%i==0:
            print(f"{f} is not prime number")
    else:
        print(f"{f} is prime number")


start = int(input("Enter start range: "))
end = int(input("Enter end range: "))
lst = []
for n in range(start, end + 1):
    if n>1:
        for i in range(2, int(n**0.5)+1):
            if n%i==0:
                break
                
        else:
            lst.append(n)
print(f"prime numbers are: {lst}")





start = int(input("Enter the start range: ")) 
end = int(input("Enter end range: "))

prime = []
not_prime = []

for i in range(start, end +1):
    if i>1:
        for n in range(2, int(i**0.5)+1):
            if i%n==0:
                not_prime.append(i)
                break
                
        else:
            prime.append(i)
print(f"The prime Numbers are: {prime}")
print(f"The Numbers are not prime: {not_prime}")




# 3. Reverse an integer using a loop.

f = int(input("Input a Integer: "))

rev = 0
temp = f

while temp>0:
    digit = temp%10
    rev = rev*10+digit
    temp = temp//10
print(rev)


f = int(input("Input a Integer: "))

rev = 0
temp = f

counts = len(str(f))

for i in range(counts):
    digit = temp%10
    rev = rev*10+digit
    temp //=10
print(rev)




