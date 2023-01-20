#3. Write a python program to reverse the tuple.
t=(1,2,3,"java","python","SQL","C")
i=len(t)-1
while i>=0:
    print(t[i],end=",")
    i=i-1