"""6. Write a python program to append elements from another list to the current list.(
firstlist = ["Java", "Python", "SQL"] ,secondlist = ["C", "Cpp", "NoSQL"] )"""
from re import L


L1 = ["Java", "Python", "SQL"] 
L2 = ["C", "Cpp", "NoSQL"]
for x in L1:
    L2.append(x)
print(L2)