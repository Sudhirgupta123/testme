#6. Write a python script to calculate factorial of a given number
n=int(input("enter a number\n"))
i=1
factorial=1
while(i<=n):
    factorial=factorial*i
    i+=1
print("sum",factorial)