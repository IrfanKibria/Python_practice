# f = open(r"C:\Users\devil\Desktop\Intro.txt","r")
# x = f.read()
# print(x)
# print(type(x))
# f.close()



# a = open(r"C:\Users\devil\Desktop\Intro.txt", "w")
# a.write("I am Eding my summary again. \n I am son of golam azam Kibira and Meherunnesa. \n I am from kishoreganj")
# print(a.read())
# a.close()



# a = open(r"C:\Users\devil\Desktop\Intro.txt","a")
# a.write("\nCurrently I live in Uttara")
# a.close()


# a = open(r"C:\Users\devil\Desktop\Intro.txt","a+")
# print(a.read())
# a.write("\nBut I need to move to a cheaper place")

# a.close()






# with open(r"C:\Users\devil\Desktop\Intro.txt", "r") as f:
#     data = f.read()
#     print(data)

# new_data = data.replace("cheaper", "expensive")
# print(new_data)

# with open(r"C:\Users\devil\Desktop\Intro.txt", "w") as e:
#     e.write(new_data)



count = 0
with open(r"C:\Users\devil\Desktop\New Text Document.txt", "r") as f:
    data = f.read()
    nums = data.split(",")
    for val in nums:
        if int(val) % 2 == 0:
            count += 1
    print(count)

