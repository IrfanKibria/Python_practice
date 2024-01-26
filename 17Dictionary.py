'''
1. Dictionary are using key value pairs to store values
2. They are made by using s1={ "key": "value", "key": "value" } syntax
3. you can get all keys of dictionary by s1. keys( )
4. you can get all values of dictionary by using s1.values( )
5. you can get all pairs of dictionary by s1.items( )
6. you can get the value of an item by using s1['key'] and it will return the value. s1.get("key") will also return 
the value but it wont throw an error in case there is no value/key available in the dictionary
'''

emp_id_with_name= {
    1: 'irfan',
    2: 'kibria',
    3: 'rafsan',
    25: 'anik',
    45: 'atiq'
}

print(emp_id_with_name[25]) # Print the value of key 25. in this case it will give error if key name doesnt exist
print(emp_id_with_name.get(25)) # Print the value of key 25. in this case it will not give error if key name doesnt exist
print(emp_id_with_name.keys())#print all the keys of existing dictionary
print(emp_id_with_name.values())#print all the keys of existing dictionary

for i in emp_id_with_name.keys():
    print(f"For {emp_id_with_name[i]} employee id is {i}") # get the emp_id for all employee


print(emp_id_with_name.items())# by this we get the key and values in tuple pairs.
for empid, empname in emp_id_with_name.items(): # by this we extract the tuple and get values
    print(f"According to {empid} employee id the employee is {empname}")



em_list = {1: 'irfan', 2: 'kibria', 3: 'talha', 4: 'imran', 5: 'gausul'}#value can be duplicate but if key is duplicate then always count the last one.
em_list2 = {6: 'mash', 7: 'hasan', 8: 'joy'}
print(em_list)
em_list.update(em_list2)#by this em_list2 will be updated in em_list.
print(em_list)
      
print(em_list)
em_list.pop(1)#it will remove 1: 'irfan' pair from the dictionary
print(em_list)

del em_list[2]# it will del 2: 'kibria' pair from dictionary
print(em_list)

print(em_list)
em_list.popitem()#it will remove last pair of existiing dictionary
print(em_list)

em_list.clear()# by this we can clear all data of a dictionary
print(em_list)

empt = {}# create a empty dictionary
print(empt)

del em_list # by this we can delete a dictionary 