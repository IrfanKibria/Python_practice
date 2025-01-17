'''List can modified. we can insert, delete data from a list
1)List bracket type: [ ] 
2)List are mutable: elements can be added, removed and be replaced 
3)Both int and string can be in a same list 
4)Slicing can be done in strings and list'''


a = [1,2,3,4,5,6,7,8,9,10,11]
print(type(a))
print(a[0])
print(a[1])
print(a) #print full list
print(a[:]) #print full list
print(a[2:5])#print index 2 to 5-1
print(a[2:-6])#in neg indexing we have to make neg to positive by sub from len.len is 10. this will print 2 to 4
print(a[1:8:2])#jump index it will printing one index after data


mlist = [i for i in range(10)]#this is called list comprehension. 
print("mlist",mlist)


mlist = [i*i for i in range(10)]
print(mlist)


mlist = [i*i for i in range(10) if i%2==0]
print("mlist 2",mlist)



b = list(map(int, input("Enter a List: ").split()))
print(b)


l =[45,56,1,5,9,12,45,15,18,11,1]
print(l)

l.reverse()#Reverse the list
print(l)

l.sort()#list will show in accending order
print(l)

l.sort(reverse=(True))#list will show in decending order
print(l)

print(l.index(9))#print the index number of 9

print(l.count(1))#print the count how much time the listt has 1

# m = l# this is not the correct way to copy list. m is a reference of l. if l change then m will be change.
# m[0] = 0
# print(m)

m = l.copy()# correct way to copy a list. here we copy l list to m list
m[0] = 0
print(l)
print(m)


l.append(100)# insert a data in a list. 100 will insert at the last
print(l)

l.pop(10)#remove index 10 from the list
print(l)

l.insert(0, 200)#insert 200 in the list at 0 index
print(l)


p = [1000, 2000, 3000]#here p list will connect with l.
l.extend(p)
print(l)

k = l+p#create a list by sub 2 list
print(k)