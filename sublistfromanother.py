#WAP to subtract a list from another list.

l1=[]
l2=[]
n1=int(input("Enter number of elements in list 1:"))
for i in range(n1):
    l1.append(int(input("Enter element:")))
print(l1)
for i in range(n1):
    l2.append(int(input("Enter element:")))
print(l2)
for i in range(n1):
    l1[i]=l1[i]-l2[i]
print("Subtracted list:",l1)
