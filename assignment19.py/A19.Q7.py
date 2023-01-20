#7. Write a python program to sum all the numbers in a list
def sum_arg(*arg):
    print(sum(arg))
l=[1,2,3,5,5,6,3]
sum_arg(*l)    