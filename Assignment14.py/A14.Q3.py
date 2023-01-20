#3. Write a Python script to create a list of first N even natural numbers.
L=[]
n=int(input("enter a number\n"))
for x in range(0,n):
    L.append(2*x)
print(L)    
