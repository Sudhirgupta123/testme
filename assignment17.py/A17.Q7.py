#7. Write a python program to remove last item of the given set thisset = {"Python", "Django", "JavaScript", “SQL”}
from os import remove


thisset = {"Python", "Django", "JavaScript", "SQL"}
thisset.remove("SQL")
print(thisset)
