#5. Write a python script to print first N odd natural numbers in reverse order
n=int(input("enter a number"))
for x in range(n+1):
    print(2*n-(2*x+1))