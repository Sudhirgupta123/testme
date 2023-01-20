#8. Write a python script to check if a string contains only numbers.
from operator import index


S=input("enter a string\n")


if S.isnumeric()==True:
    print("string have only number")
else:
    print("string contains alpha numeric")