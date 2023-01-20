#3. Write a recursive python function to calculate sum of first N even natural numbers
def even_num_sum(n):
    if n==1:
       return 2
    else:
        return (2*n)+even_num_sum(n-1)
p=even_num_sum(7)           
print(p)