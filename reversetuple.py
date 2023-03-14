#Reverse a tuple.

l=[]
n=int(input("Enter number of elements:"))
for i in range(n):
    l.append(input("Enter element:"))
t=tuple(l)
print("Tuple:",t)
for i in range(len(l)//2):
    l[i],l[len(l)-1-i]=l[len(l)-1-i],l[i]
print("Tuple after reversing:",tuple(l))
    
