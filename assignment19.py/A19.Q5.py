#5. Write a python program to create a function which expects a list as an argument.
def list_argument(*args):
    print(args)
l=["sudhir","saurabh","vinay",10,230,44]
list_argument(*l)    