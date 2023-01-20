'''5. Write a python script to create a Calculator class with 2 methods for adding and
subtracting 2 values.'''



class calculator:

    def adding(self,a,b):
        c=a+b
        print(c)           
    def subtracting(self,a,b):
        d=a-b
        print(d) 
obj1=calculator()
obj1.adding(10,5)
obj1.subtracting(10,5)
