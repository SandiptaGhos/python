#Approximate the tuple values.

l=[]
n=int(input("Enter number of elements:"))
for i in range(n):
    l.append(float(input("Enter element:")))
t=tuple(l)
print("Original Tuple:",t)
for i in range(len(l)):
    d=l[i]
    l[i]=round(d)
print("Approximated values:",tuple(l))



                   
