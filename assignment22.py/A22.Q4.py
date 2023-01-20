#4. Write a recursive python function to calculate sum of squares of first N natural numbers

def sqr_sum(n):
    if n==1:
       return 1
    else:
        return (n**2)+sqr_sum(n-1)
p=sqr_sum(4)           
print(p)