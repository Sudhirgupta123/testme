#4. Write a python script to calculate sum of first N odd natural numbers
n=int(input("enter a number\n"))
i=0
sum=0
while i<=n:
    sum=sum+(2*i+1)
    i+=1
print("sum=",sum)    
