#8. Create an endless iterator using generator method to produce Prime numbers



def endless_iterator(p):
  i=2
  while i<p:
      if p%i==0:
        yield("not prime")
        break
      i=i+1          
  else:
        yield("prime")
      

list=[]          
while True:        
    if (input("do you want to chek a number is prime or not[y/n]\n")=="y"):
      list.append(next(endless_iterator(int(input("enter a number\n")))))  
    else:
      break
print(list)    
