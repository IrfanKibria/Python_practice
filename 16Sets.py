'''
1. Sets are collection of well defined data type.
2. Set in python is made by { }
3. all functions of list are applicable to sets
4. sets and lists are different in only that a set does not allow repetition of same entry while in list you can repeat the same item.
5. Empty set is made by Emptyset= ( ) instead of { }
6. There is no guaranttee of order being maintained by Python within a set so output can change every time. (bummer)
7. To get items you can use for loop just like a list.
'''


set_a = {10, 5, 45, 50, True, 'talha', 'kibria', 1, 8, 5, False}
print(f"type of this is {type(set_a)} and the set is {set_a}")

# for value in set_a:
#     print(value)


'''Create a empty set. if use just {} then it will be empty dic. we have to use set()'''

irfan = set()
print(type(irfan))

kibria = {}
print(type(kibria))

'''opreration on sets'''

a = {1,3,4,5}
b = {7,8,4,5}
h1 = a.union(b) # here we are perform unioin between a and b and store in a new set named h1. and print it.
print(h1)

c = {1,3,4,5}
d = {7,8,4,5}
c.update(d)# by this we are update c to exsting c set. the unique values of c and d store in c.
print(c)

e = {1,3,4,5}
f = {7,8,4,5}
h2 = e.intersection(f)# here we are perform intersection between e and f and store in a new set named h2. and print it.
print(h2)


g = {1,3,4,5}
h = {7,8,4,5}
g.intersection_update(h)# by this we are update g to exsting g set. the unique values of g and h store in g.
print(g)


i = {1,3,4,5}
j = {7,8,4,5}
h3 = i.symmetric_difference(j)#by this function we can find out which elements are not same in 2 sets. calc is (A Unioin B) - (A Intersaction B)
print(h3)

k = {1,3,4,5}
l = {7,8,4,5}
k.symmetric_difference_update(l)#by this function we can find out which elements are not same in 2 sets. calc is (A Unioin B) - (A Intersaction B)
print(k)


m = {1,3,4,5}
n = {7,8,4,5}
h4 = m.difference(n)#by this we can see which elements are not having in n set
print(h4)


o = {1,3,4,5}
p = {7,8,4,5}
h5 = o.isdisjoint(p)#it checks is two set has any common elements or not. if there is no common element then it will print true. if has common values then return false.
print(h5)

q = {1,3,4,5}
r = {7,8,4,5}
h6 = q.issuperset(r)#it check if the r set's elements are available in q set. if all the elements of r are contains in q set then it will return true nither it will return false.
print(h6)



q = {1,3,4,5}
r = {1,4,5}
h7 = r.issubset(q)#it check is r's all element are common in q. then r is subset of q.
print(h7)


s = {1,3,4,5}
s.add(10)
print(s)

t ={11, 12}
s.update(t)# it will update s set. the elements of t will store to s. s will update with t's element.
print(s)

s.remove(3)
print(s)

s.discard(1)#discard and remove are similar but difference is remove will give error if the element is not present in existing set. but discard will not rais any error if the element is not present in the set.
print(s)

h8 = s.pop()#by this the last element of set will removed. it will give manupulative return because set is not organized. which element will remove we can not say.
print(h8,s)


u = {1,3,4,5,6,7,9}
print(u)
u.clear()# if we want clear all the elements of a set then we use clear
print(u)

del u#by this we delete u set completly

'''Checking a number if it is present in a set'''
user_input = int(input("Enter a number: "))
t = {1,3,4,5,6,7,8}
if user_input in t:
    print(f"{user_input} is present in t")
else:
    print(f"{user_input} is not present in t")

