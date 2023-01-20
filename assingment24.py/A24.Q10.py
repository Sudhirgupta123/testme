'''10. Define a class Employee with instance object variables empid, name, salary. Write
__init__() method in the class to initialize instance object variables. Also define
instance methods to input fields and display field values'''

class Employee:
    def __init__(self,empid,name,salary):
        self.empid= empid
        self.name=name
        self.salary=salary
    
    def company(self):
        print(self.empid)
        print(self.name)
        print(self.salary)
        
obj1=Employee(33,"sudhir",45566)
obj1.company()        


