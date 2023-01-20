#3. Write a recursive python function to print first N odd natural numbers
def oddN(n):
    if n==0:
       return 1
    else:
        oddN(n-1)
        print(2*n-1)   
oddN(10)                