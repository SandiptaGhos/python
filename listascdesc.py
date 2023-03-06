#WAP to check if the given list is in ascending order or descending order

lst=[]
lst1=[]
lst2=[]
n=int(input("Enter the number of elements in a list:"))
for i in range(0,n):
    element=int(input())
    lst.append(element)
lst1=lst.copy()
lst1.sort()
lst2=lst.copy()
lst2.reverse()
if(lst1==lst):
    print("The list is in Ascending order")
elif(lst2==lst):
    print("The list is in Descending order")
else:
    print("The List is not sorted")
    
