#3. Write a python script to calculate sum of cubes of first N natural numbers
n=int(input("enter a number\n"))
i=1
sum=0
while i<=n: 
    sum=sum+i**3
    i=i+1
print("sum",sum)