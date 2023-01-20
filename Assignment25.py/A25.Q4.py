#4. Write a python script to update 2nd Question, add a class variable (platform) and create a classmethod to access it.

class profile:
    name="sudhir"
    email="guptas3333@gmail.com"
    age="23"
    platform="ineuron"
    
    def classmethod(self):
        print(self.name)
        print(self.email)
        print(self.age)
        print(self.platform)
p=profile()
print(p.classmethod())