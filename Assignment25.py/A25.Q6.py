'''6. Write a python script to create a Calculator 2.0 class with 2 methods for multiplication
and division of 2 values and inherit it from the Calculator class.'''



from tkinter import E


class calculator:

    def adding(self,a,b):
        c=a+b
        print(c)           
    def subtracting(self,a,b):
        d=a-b
        print(d) 
class calculator2(calculator):
    def multiplication(self,a,b):
        f=a*b
        print(f)
    def division(self,a,b):
        E=a/b
        print(E)

obj1=calculator()
obj2=calculator2()
obj2.adding(10,5)
obj2.subtracting(10,5)
obj2.multiplication(10,5)
obj2.division(10,5)
