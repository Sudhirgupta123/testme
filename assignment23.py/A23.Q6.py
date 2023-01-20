#6. Create a generator to produce first n prime numbers



def primenumber(n):
    i=2
    while n>i:
        if n%i==0  :
            yield ("not prime number at =",i)
            break
        else:
            yield("prime",n,i)    
        i=i+1        
for p in primenumber(int(input("enter a number\n"))):
    print(p)                    


