''' strings are immutable but we can make a copy with some changes.
Here are Some Methods are for Uppercase, Lower case, Capitalize, split,
Count, rstrip, replace, endswith ect'''

a = input("Enter a string: ")

b = a.upper()
x = a.lower()
y = a.capitalize()
m = a.split(" ")
v = a.count("a")
print(v)
print(m)
print(y)
print(x)
print(b)



c = input("enter a name: ")
print(c.split(" "))
print(c.capitalize())
print(c.upper())
print(c.lower())
print(c.count("a"))

#rstrip does remove leading symbol
name = "Irfan########"
a_name = name.rstrip("#")
print(a_name)


name1 = name.replace("Irfan", "Kibria")
print(name1)

print(name1.replace("Kibria", "talha"))

print(name.endswith("####"))

print(name.endswith("an", 0, 5))

print(name1)