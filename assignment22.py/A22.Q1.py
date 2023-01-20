#1. Write a recursive python function to calculate sum of first N natural numbers
def sum(n):
    if n==1:
        return 1
    else:
        return  n+sum(n-1)
p=sum(5)
print(p)

