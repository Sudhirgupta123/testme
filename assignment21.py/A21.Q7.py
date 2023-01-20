#7. Write a recursive python function to print squares of first N natural numbers
def sqr(n):
    if n==0:
        return 1
    else:
        sqr(n-1)
        print(n*n)
sqr(10)            