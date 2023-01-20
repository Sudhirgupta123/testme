#7. Write a recursive python function to calculate sum of the digits of a given number
def Sum_of_digit(n):
   p=int(input("enter a number\n"))
   sum=0
   while p>0:
       sum=sum+p%10
       p=p//10
   print(sum)
   if n==1:
    return 1 
   else:
     return Sum_of_digit(n-1) 
    
t=Sum_of_digit(3)        
# print(t)