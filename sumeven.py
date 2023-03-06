minimum=int(input("Enter minimum value :"))
maximum=int(input("Enter maximum value :"))
total=0
for number in range(minimum,maximum+1):
    if(number%2==0):
        total=total+number
print("The sum of Even Numbers from 1 to {0}={1}".format(number,total))
    
