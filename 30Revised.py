'''1st step coding. Printing & Variables, Data Type'''

print("Irfan")

print("Talha")

print("Irfan","Talha")

x = "Irfan Kibria "
y = "Talha"
print(x+y) 

u = 25.5
v = 27
z = True
print(type(v), type(u) ,type(x), type(z))


'''Input, String concatenation, Input , & comments'''

name = input("Enter Your Name: ")
print("Hello", name)
print("Hello" + name) #string concatenation


"""Excersise"""

super_hero_name = input("Name you super hero: ")
super_hero_age = int(input("Enter super hero age: "))
super_hero_power = str(input("power: "))

print(f"{super_hero_name}\n{super_hero_age}\n{super_hero_power}")


# type casting & type conversion

print(1+2.5)#type convertoin. Because python autometicty output the result as float. Implicit. 

print(float(2)+ 2)#type cationg because we change the type using float function. Explicit