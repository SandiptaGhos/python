#convert a tuple into a string

l=[]
n=int(input("Enter number of elements:"))
for i in range(n):
    l.append(input("Enter element:"))
t=tuple(l)
print("Tuple:",t)
s="".join(t)
print("String:",s)
