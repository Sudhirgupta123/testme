#. Write a python program to access a function inside a function
def add(n):
   if n==1:
     return(1)
   else:  
     return(n+add(n-1))
p=add(6)
print(p)     