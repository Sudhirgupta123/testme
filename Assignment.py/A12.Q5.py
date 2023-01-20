#5. Write a python script to find next prime number of a given number
n=int(input("enter a number\n"))

for x in range(3,n): 
  i=2
  while i<x:
      if x%i==0:
          break
      i=i+1
  else:
      print("number is prime",x) #Doubt
      
   