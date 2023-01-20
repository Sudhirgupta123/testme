#9. Write a recursive python function to print first N multiples of a given number.
def multiples(n):
    i=1
    while i<=n:
        if i==1:
            return 1
        else:
            print(i*multiples(n-1))
        i=i+1    
multiples(18)                
