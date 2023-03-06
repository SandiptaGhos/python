minimum=int(input("Enter minimum value :"))
maximum=int(input("Enter maximum value :"))
oddtotal=0
for number in range(minimum,maximum+1):
    if(number%2!=0):
        oddtotal=oddtotal+number
print("The sum of Odd Numbers from 1 to {0}={1}".format(number,oddtotal))
    
