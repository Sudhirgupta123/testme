#9. Write a python program to create a School class and 3 instance variables and 1 class variable.
from email.headerregistry import Address


class School:
   roll_no=34
   def student(self):
    name="sudhir" 
    Address="mau"
    college="gcet"
    self.c=self.roll_no
    print(self.c)
    print(name)
    print(Address)
    print(college)

    
object=School()
print(object.student())






