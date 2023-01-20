#5. Create a generator to produce first n terms of Fibonacci series
def Febonacci(n):
    i,j=0,1
    while n:
        yield i
        i,j=j,j+i
        n=n-1
for i in Febonacci(10):
    print(i,end=" ")       