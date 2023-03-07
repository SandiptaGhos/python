#WAP to merge two list

l1=[]
l2=[]
n1=int(input("Enter number of elements in list 1:"))
for i in range(n1):
    l1.append(int(input("Enter element:")))
print(l1)
n2=int(input("Enter number of elements in list 2:"))
for i in range(n2):
    l2.append(int(input("Enter element:")))
print(l2)
l3=l1+l2
print("Merged list:",l3)
