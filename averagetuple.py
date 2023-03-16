#Find the average values of the tuple elements.

l=[]
n=int(input("Enter number of elements:"))
for i in range(n):
    l.append(int(input("Enter element:")))
t=tuple(l)
print("Tuple:",t)
print("Average:",sum(t)/len(t))
