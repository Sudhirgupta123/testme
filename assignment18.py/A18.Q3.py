#3. Write a python program to get a list of the values from a dictionary

from multiprocessing.sharedctypes import Value


D={"name":"sudhir","age":21,"address":"mau"}
Value=[]
for i in D.values():
    print(i)
    p=Value.append(i)
print(p)

