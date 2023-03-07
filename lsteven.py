lst=[]
n=int(input("Enter number of elements in a list:"))
for i in range(0,n):
    element=int(input())
    lst.append(element)
for i in range(0,n):
    if (lst[i]%2==0):
            print(lst[i])
            
