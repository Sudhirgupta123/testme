#4. Write a python script to print all Prime numbers between two given numbers (both values inclusive)
n,m=int(input("enter starting num\n")),int(input("enter last number\n"))
for x in range(n,m):
  i=2
  while i<n:  
    if x%i==0:
       break
    i=i+1
  else:
       print("number is prime",x)