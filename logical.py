a=int(input("Enter the number a :"))
b=int(input("Enter the number b: "))

c=(a>b)and(a<b)
print ("The logical opertion of AND is :", c)

d=(a>b)or(a<b)
print ("\n The logical operation of OR is : ", d)

e=not(a>b)
print("\n The logical operation of NOT is : ", e)