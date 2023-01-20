#8. Write a Python script to print distinct elements along with their frequencies of occurrence in the list.
from itertools import count


l=["sudhir","prince","praveen","shivam","sudhir","prince","praveen","sudhir","prince","praveen"]
p=set(l)
for i in p:
    x=l.count(i)
    print(x,i)