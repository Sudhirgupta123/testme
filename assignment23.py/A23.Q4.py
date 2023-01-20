#4. Create a generator to produce squares of first N natural numbers
def  sqr(n):
  x=0
  while n:
    yield x**2
    x=x+1
    n=n-1
for i in sqr(10):
    print(i)    

