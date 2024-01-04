# for i in range(20000):
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
        


