'''. Write a python program to add elements of list to a set thisset = {"Python", "Django", "JavaScript"}
mylist = ["Java", "C"]
'''
thisset = {"Python", "Django", "JavaScript"}
mylist = ["Java", "C"]
p=set([*thisset]+mylist)
print(p)