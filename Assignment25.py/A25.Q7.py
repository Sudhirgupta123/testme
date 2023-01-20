'''7. Write a python script to create a Phone class with 2 methods to print the features
(calling and sms).'''

class phone:
    def calling(self,mobile_number):
        p=mobile_number
        print("uou are calling on this num.=",p)
    def sms(self,WriteSms):
        S=WriteSms
        print("your massege is =",S)
obj1=phone()
obj1.calling(9140902575)
obj1.sms("hallo every one how are you")            