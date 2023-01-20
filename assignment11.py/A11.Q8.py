#8. Write a python script to calculate sum of digits of a given number
n=int(input("enter a number"))
s=0
while n!=0:
    i=n//10
    s=s+n%10
    print(s)