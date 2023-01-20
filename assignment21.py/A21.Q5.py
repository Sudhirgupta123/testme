#5. Write a recursive python function to print first N even natural numbers.
def evenN(n):
    if n==0:
        return 1
    else:
        evenN(n-1)
        print(2*n)
evenN(10)              
