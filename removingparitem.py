#Remove a particular item in a item.

l=[]
n=int(input("Enter number of elements:"))
for i in range(n):
    l.append(input("Enter elements:"))
t=tuple(l)
print("Tuple:",t)
ch=int(input("Enter index to be removed:"))
l.pop(ch)
print("Tuple after removing element:",tuple(l))

