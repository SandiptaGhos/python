#WAP to interchange the 1st element and last element in a list.

lst=[]
n=int(input("Enter the no. of elements in a list:"))
for i in range(0,n):
    element=int(input())
    lst.append(element)
print(lst)
a=lst[0]
b=lst[n-1]
lst[0]=b
lst[n-1]=a
print(lst)
