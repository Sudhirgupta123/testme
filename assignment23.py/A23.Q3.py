#3. Create a generator to produce first n even natural numbers
from re import X
def evennaturalnumber(n):
  x=2
  while n:
   yield x
   x=x+2
   n=n-1
for i in evennaturalnumber(14):
    print(i)
