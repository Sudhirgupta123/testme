#8. Write a python script to print first N terms of a Fibonacci series
from operator import truediv

n=int(input("enter a number\n"))
a,b=0,1
i=0
while i<n:
    a,b=b,a+b
    print(b,end=" ")
    i=i+1