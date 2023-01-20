#2. Create a generator to produce first n odd natural numbers
def oddnatural(n):
  x=0
  while n:
    yield 2*x+1
    x=x+1
    n=n-1
for o in oddnatural(10):
   print(o)

