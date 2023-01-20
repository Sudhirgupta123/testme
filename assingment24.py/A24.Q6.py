#6. Write a python program to create 3 user objects and find the youngest of all.

class user:

    def UserAge(self,age):
        a=age
        return a
        
    def UserAge1(self,age1):
        b=age1 
        return b
        
    def UserAge2(self,age2):    
        c=age2
        return c  
obj=user()
p=obj.UserAge(50)
q=obj.UserAge1(40)
r=obj.UserAge2(30)
if p>q>r:
    print("p is youngest " )
elif q>r>p:
    print("q is youngest " ) 
else:
    print("r is youngest ")       
