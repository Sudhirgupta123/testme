#6. Write a recursive python function to print first N even natural numbers in reverse orderdef evenN(n):
def reverce_even(n):
    if n==0:
        return 1
    else:
        print(2*n)
        reverce_even(n-1)
       
reverce_even(10)  