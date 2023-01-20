# 8. Write a python script to create a SmartPhone class by inheriting Calculator 2.0 and Phone Class.

from tkinter import N


class calculator:

    def adding(self,a,b):
        c=a+b
        print("addition=",c)           
    def subtracting(self,a,b):
        d=a-b
        print("substraction=",d) 
class calculator2(calculator):
    def multiplication(self,a,b):
        f=a*b
        print("multiplication=",f)
    def division(self,a,b):
        E=a/b
        print("division",E)

class phone:
    def calling(self,mobile_number):
        p=mobile_number
        print("uou are calling on this num.=",p)
    def sms(self,WriteSms):
        S=WriteSms
        print("your massege is =",S)        

class smartPhone:
    def Smart_phone(self):
        N="your smart phone can do multiple work"
        print(N)

object=smartPhone()
object.Smart_phone()        


obj1=calculator()
obj2=calculator2()
obj2.adding(10,5)
obj2.subtracting(10,5)
obj2.multiplication(10,5)
obj2.division(10,5)

obj3=phone()
obj3.calling(9140902575)
obj3.sms("hallo every one how are you")     
       
