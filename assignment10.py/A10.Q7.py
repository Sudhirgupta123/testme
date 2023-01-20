#7. Write a python script to print first N even natural numbers in reverse order
N=int(input("enter the natural number"))
for x in range(N+1):
    print((2*N-1)-(2*x-1))