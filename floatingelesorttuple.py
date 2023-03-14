#shot a tuple which contains  floating elements.

l=[]
n=int(input("Enter number of elements:"))
for i in range(n):
    l.append(float(input("Enter elements:")))
t=tuple(l)
print("Tuple:",t)
print("Sorted tuple:",sorted(t))
