'''
1.When we want to make a constant, then tuple is used.
2., is added if 1 item tuple is made.
3.Tuples are ordered collection of data items. 
4.They store multiple items in a single variable. 
5.Tuple items are separated by commas and enclosed within round brackets (). 
6.Tuples are unchangeable meaning we can not alter them after creation.
7.Tuples can be sliced similar to lists but new tuple is created in the process.
8. Tuples and strings both are immutable.
'''

tup1 = (1, 5, 4,68,34, "Irfan")
print(f"{type(tup1)}, {tup1}")
print(tup1[3])
print(tup1[-2])
print(tup1[0:5:2])


'''indirectly we can change the tupple. direcly we cannot change the tupple.'''

lan = ("Bangla", "Hindi", "English", "German")
print(lan)

temp_lan = list(lan)#make the tupple a list first
temp_lan.append("Russain")#add a language in the list
print(temp_lan)
temp_lan.pop(0)#remove 0 index from the list
print(temp_lan)
temp_lan.insert(0, "Spaning")#insert a language in 0 index on the list
print(temp_lan)
temp_lan[3] = "French"#modified the index 3 data to french
print(temp_lan)
lan = tuple(temp_lan)#make the list into tupple and assaign to existing tupple
print(lan)
