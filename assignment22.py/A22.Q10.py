#10. Write a recursive python function to find the Nth term of the Fibonacci series
#0,1,1,2,3,5,8.....
def febonacci(n):
   i,j=0,1
   if i!=j:
    return j+febonacci(n-1)
p=febonacci(5)        
print(p)