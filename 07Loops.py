# for i in range(20000):
#     print(i)


# for i in range(0,100,5):
#     print(i)


# name = ["IRfan", "Kibria", "Talha"]
# for i in name:
#     print(i)
#     for z in i:
#         print(z)
    



name = input("Input Your name: ")

count = 0
for i in name:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        print(i, end=", ")
        count = count +  1

print(f"No of vowels {count}")
        


text = input('Enter text: ')

for char in text:
    if char in 'aeiouAEIOU':
        print(char,'is vowel')
    else:
         print(char,'is Consonant')






# 6. Keep taking user input in a list until 'exit' is typed.
list_a = []
while True:
    f = input("Enter a Number: ")
    if f.lower() == 'exit':
        break
    list_a.append(f)
print(list_a)


# 6. Keep taking user input in a list until 'exit' is typed.
list_a = []
for i in iter(int, 1):
    f = input("Enter a Number to add in a list: ")
    if f.lower() == 'exit':
        break
    list_a.append(f)
print(list_a)



# Write a problem where take a range from user for list and take list elements from user
n = int(input("Enter the range of list"))
list_a = []
for i in range(n):
    f = input("Enter a Number to add in a list: ")
    if f.lower() == 'exit':
        break
    list_a.append(f)
print(list_a)