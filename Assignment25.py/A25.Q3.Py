# 3. Write a python script to update 2nd Question, change email and age to __email and __age.
class profile:
    __name="sudhir"
    __email="guptas3333@gmail.com"
    __age="23"
    
    def __init__(self):
        print(self.__name)
        print(self.__email)
        print(self.__age)
p=profile()
print(p.age)