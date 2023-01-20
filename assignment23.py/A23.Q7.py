#7. Create an endless iterator using generator method to produce terms of Fibonacci series


def fibonacci():
   i,j=0,1
   while True: 
      yield i
      i,j=j,i+j
      
p=fibonacci()
it=[]
while True:
   if input("Do you want genrate a number [y/n]\n")=='y':
     it.append(next(p))
   else:
     break  
print(it)    