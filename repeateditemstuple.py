#Find the repeated items in a tuple.

l=[]
n=int(input("Enter number of elements:"))
for i in range(n):
    l.append(input("Enter element:"))
t=tuple(l)
print("Tuple:",t)
lt=[]
print("Repeated elements:",end=" ")
for i in t:
    if i not in lt:
        lt.append(i)
    else:
        print(i,end=" ")
        
             
