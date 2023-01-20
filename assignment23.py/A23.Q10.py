"""10. Define a function which calculates HCF of two numbers. Define and apply a
decorator to check whether two given numbers are co-prime or not"""

# n3=int(input("enter a number\n"))
def HCF(n1,n2):
    if n1>n2:
        smaller=n2
    else:
        smaller=n1
    for i in range (2,smaller+1):
        if (n1%i==0 and n2%i==0):
            hcf=i
        return hcf 
print()
print(HCF(int(input("enter a number\n")),int(input("enter a number\n"))))        
            



            


