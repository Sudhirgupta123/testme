#4. Write a recursive python function to print first N odd natural numbers in reverse order
def odd_reverce(n):
    if n==0:
        return(1)
    else:
        print(2*n-1)
        odd_reverce(n-1)
odd_reverce(10)            
