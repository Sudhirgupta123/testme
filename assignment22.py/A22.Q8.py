#8. Write a recursive python function to print binary of a given decimal number.
def binary(n):
   if n==1:
      return(bin(n))
   else:
    return binary(n-1)
p=binary(10)   
print(p)
###########################################doubt