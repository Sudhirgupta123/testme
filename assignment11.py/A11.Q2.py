#2. Write a python script to calculate sum of squares of first N natural numbers

number=int(input("enter a number"))
i=1
n=0
while i<=number:
   n=n+i**2
   i+=1
print("sum=",n)
