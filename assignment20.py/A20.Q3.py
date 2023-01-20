'''3. Write a python program to create a function that prints the even numbers from a
given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]'''
def print_even_no(l):
    for i in l:
        if i%2==0:
            print("even number",i)
        else:
            pass

print_even_no([1, 2, 3, 4, 5, 6, 7, 8, 9])            

