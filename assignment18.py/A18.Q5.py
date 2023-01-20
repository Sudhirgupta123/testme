#5. Write a python program to print all key names in the dictionary, one by one.
from re import L


D={"name":"sudhir","age":21,"address":"mau"}
L=[]
for i in D.keys():
    L.append(i)
    print(i)