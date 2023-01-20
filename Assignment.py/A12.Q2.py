#2. Write a python script to check whether a given number is Prime or not
n=int(input("enter a number\n"))
i=2
while i<n:
      if n%i==0:
          print("n is not prime")
          break
      i=i+1
      
else:
    print("n is prime")    