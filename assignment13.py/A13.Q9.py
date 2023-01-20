#9. Write a Python script to create a list of city names taken from the user.
L=[]

ls=int(input("enter list element size\n"))

i=1
while i<ls:
   L.insert(i,input("enter citys name\n"))
   i=i+1
print(L)
   
   