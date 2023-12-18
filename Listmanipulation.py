List1=[10,20.3,True,False,'Hello']

print("Modifing the Element :")
List1[1]=66
print(List1)

print("Extending the list :")
List1.extend([45,67])
print(List1)

print("Inserting the element:")
List1.insert(3,50)
print(List1)

print("Popping the last Element :")
List1.pop()
print(List1)

print("Popping the particluar position number : ")
List1.pop(1)
print(List1)

print("The length of the list:")
print(len(List1))

print("The number of count of element: ")
print(List1.count(50))

print("Reverse of a List")
List1.reverse()
print(List1)

print("Sorting the Elements")
l=[9,0,1,45,2,3,67,94,2]
l.sort()

print("Coping the elements")
l1=l.copy()
print(l1)

print("Clearing the List:")
l.clear()
print(l)