'''2. Write a python program to create a function that takes a number as a parameter and
checks if the number is prime or not.'''
def prime(n):
    
  if n>1:  
    for x in range(2,n):
         if n%x==0:
             print("number is not prime")
             break   
    else:
         print("prime")
  else:
      print("prime")     
              
               
prime(int(input()))
