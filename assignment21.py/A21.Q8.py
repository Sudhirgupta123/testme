#8. Write a recursive python function to print cubes of first N natural numbers
def sqr(n):
    if n==0:
        return 1
    else:
        sqr(n-1)
        print(n*n*n)
sqr(10)    