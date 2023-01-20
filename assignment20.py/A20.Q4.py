'''5. Write a python program to create a function that checks whether a passed string is
palindrome or not.'''
from audioop import reverse
from re import T


def pelindrome(s):
    i=0
    while i<len(s):
        if s[i]==s[-(i+1)]:
            print("pelindrome",s[i])
            
        else:
            print("not pelindrome")
            break
        i=i+1    
pelindrome(input())
