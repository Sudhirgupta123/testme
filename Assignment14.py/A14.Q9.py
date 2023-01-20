#9. Write a Python script to print indices of all occurrences of a given element in a given list.
l=[1,2,4,5,8,3,7,10,9]
for i in l:   
   p=l.index(i)
   print("index=",p,"value=",i)