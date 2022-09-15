'''Problem Statement: You have to write a Word Puzzle Game in which the user has to form
the correct word out of a given set of characters. In the game the user has to solve this
puzzle for 5 words, one at a time. Problem words are stored in a list and appear to the user
in random sequence. Give the user score +1 for each correct answer and give -1 for each
wrong answer. At last print the final score. You can store any number of words in the list, but
in each round of the game only 5 words are shown to the user.
'''
 
import random

D={"apple":"pleapa","mango":'anmgo',"umbrella":'ubrellma',"banana":'anbana',"tomato":'tmaoto','aeroplane':'oaerelanp','father':'raehtf','break':'kabre'}  
l=[]
i=0    
while i<5:     
    name=['pleapa','anmgo','ubrellma','anbana','tmaoto','oaerelanp','kabre','raehtf'] 
    c=random.choice(name)
    print(c)
    #s=set(c)     
    if (c)==D.get(input("Arrange the letters to form a valid word\n:")): #(to stop the error when we pass incorect key we 
                                                                          # can use (.get) after dictinary name then pass key.)
            print("correct")
            print()
            l.append(1)
            
    else:
            print("incorrect")
            print()
            l.append(-1)    
    i=i+1
print("final score =",sum(l))                 