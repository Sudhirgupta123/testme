#4. Write a python program to create a function which expects kwargs arguments.
def kwargs_argument(**kwags):
    for key,value in kwags.items():
        print(key,value)

kwargs_argument(a=5,b=6,c=3,d=4)      
  