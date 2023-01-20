#3. Write a python script to print all Prime numbers under 100

for n in range(3,101):
    i=2    
    while i<n:
         if (n%i)==0:
            break
         i=i+1
    else:
        print("n is prime",n)    