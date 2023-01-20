#7. Write a Python script to remove all non int values from a list.
from os import remove


l=[1.5,4,3.9,5,7.8,6,8,9.10,'sudhir','hallo',2+3j]
i=0
while i<len(l):    
    for x in l: 
      if type(i)!=type(x):
        l.remove(x)
    i=i+1 
else:
    print(l)
