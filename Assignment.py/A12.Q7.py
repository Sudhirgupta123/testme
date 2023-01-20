#7. Write a python script to check whether a given pair of numbers are co-Prime numbers or not
n=int(input("enter number1 greater then two \n"))
m=int(input("enter number2  greater then two\n"))
for x in [n,m]:
    i=2
    while i<(n):
        if x%i==0:
            print("number is not prime",x)
            break
        i=i+1
    else:
        print("number is prime",x)


      