#2. Write a recursive python function to print first N natural numbers in reverse order
def printN(n):
   if n==0:
     return 1
   else:
    print(n)

    printN(n-1)
    
printN(10)