#Convert a String and a list into tuple.

l=[]
n=int(input("Enter number of elements:"))
for i in range(n):
    l.append(input("Enter element:"))
print("List:",l)
t1=tuple(l)
print("Tuple:",t1)
s=input("Enter a string:")
ts=tuple(s)
print("Tuple:",ts)
