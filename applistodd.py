#WAP to get data items from a list appearing odd number of times.

l1=[]
n1=int(input("Enter number of elements in list 1:"))
for i in range(n1):
    l1.append(int(input("Enter element:")))
print(l1)
for i in l1:
    if(l1.count(i)%2==1):
        print(i,end=' ')
        
    
