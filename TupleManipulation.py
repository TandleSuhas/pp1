Tup=(10,20.3,'Hello',True,False,10)

print("The Length of Tuple: ")
print(len(Tup))

print("Counting the element:")
print(Tup.count(10))

print("The index of element: ")
print(Tup.index('Hello'))

#Second Tuple
Tup1=(23,44,10,3,7,20,91)
print("Sorted tuple using function :")
t=sorted(Tup1)
print(t)

print("The minimum number in tuple:")
print(min(Tup1))

print("The Maximum number in tuple:")
print(max(Tup1))

print("Adding the elments in tuple:")
t1=sum(Tup1)
print(t1)

print("Removing an element from tuple:")
print(Tup1[3]) 

print("Deleting the tuple : ")
del Tup1

