#5. Write a recursive python function to calculate sum of cubes of first N natural numbers

def cube_sum(n):
    if n==1:
       return 1
    else:
        return (n**3)+cube_sum(n-1)
p=cube_sum(4)           
print(p)