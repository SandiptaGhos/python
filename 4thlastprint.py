#Print the 4th and last element of a tuple

l=[]
n=int(input("Enter number of elements:"))
for i in range(n):
    l.append(input("Enter element:"))
t=tuple(l)
print("Tuple:",t)
print("4th element:",t[3])
print("Last element:",t[len(t)-1])
