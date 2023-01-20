#1. Use iter and next method to access all the elements of a given set using while loop


s={1,3,5,7,9,12}
i=0

p=iter(s)
while len(s)>i:
    l=next(p)
    print(l)

    i=i+1
