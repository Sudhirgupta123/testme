'''. Write a python program to create a function that accepts a string and calculate the
number of upper case letters and lower case letters.'''
def calculate_case(s):
    for i in s:
       if i.upper()==True:
        print("i is upper case",i)
       else:
        print("i is lower case",i)
calculate_case("SuDhIr")         #doubt

