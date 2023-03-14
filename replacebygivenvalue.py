#Replace the last value of a tuple by the given value of the user.

l=[]
n=int(input("Enter number of elements:"))
for i in range(n):
    l.append(input("Enter element:"))
    t=tuple(l)
print("Tuple:",t)
ch=input("Enter character:")
l[len(l)-1]=ch
print("Tuple after replacing character:",tuple(l))
