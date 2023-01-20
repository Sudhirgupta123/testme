#2. Write a recursive python function to calculate sum of first N odd natural numbers
def sum_odd(n):
    if n==1:
        return 1
    else:
        return (2*n-1)+sum_odd(n-1)    
p=sum_odd(5)
print(p)