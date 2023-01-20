'''8. WRT 7th Question, create 3 Laptop objects and add them to the list in the sorted
order based on the ram size.'''
l=[]
class laptop:
    
    def __init__(self,brand,ram,cpu,hdd):
         self.brand=brand
         self.ram=ram
         self.cpu=cpu
         self.hdd=hdd
    def showConfig(self):
        # print (self.brand)
        # print (self.ram)
        # print (self.cpu)
        # print (self.hdd)
        
        l.append(self.brand)
        l.append(self.ram)
        l.append(self.cpu)
        l.append(self.hdd)
def GetKey(obj):
    return obj.ram
l.sort(ram=GetKey)    
        

obj1=laptop('hp',"512gb","core i5","8gb") #object
obj2=laptop('realme',"512gb","core i5","4gb")
obj3=laptop('dell',"512gb","core i5","16gb")
obj1.showConfig()
obj2.showConfig()
obj3.showConfig()
# l.sort()
print(l)
