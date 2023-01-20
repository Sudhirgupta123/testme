#9. Write a python script to calculate LCM of two numbers
n=int(input("enter number1 \n"))
m=int(input("enter number2 \n"))
i=2
while i<n and i<m:
    if (n%i and m%i)==0:
        print(i)
    i+=1    #doubt10