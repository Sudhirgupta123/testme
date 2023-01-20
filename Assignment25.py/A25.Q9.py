'''9. Write a python script to create an application like Truecaller where names and
numbers are stored. Truecaller class will have 2 methods (1st to fetch the name of a
number and 2nd to add a new entry).'''

import numbers


nameList=[]
numbers=[]
class Truecaller:
    
    def contect_number(self,mobile_number):
        p=mobile_number
        numbers.append(p)
        # print("uou are calling on this num.=",p)
    def Name(self,name):
        S=name
        nameList.append(S)
        # print("your massege is =",S)        
obj1=Truecaller()

obj1.contect_number(7863627324)
obj1.contect_number(7863627387)
obj1.contect_number(7863627355)

obj1.Name("sudhir")
obj1.Name("gupta")
obj1.Name("aman")

print(nameList)
print(numbers)