# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 13:02:27 2019

@author: 17bcd7045
"""



import random 
  

  
while True: 
    print("Enter choice \n 1. Rock \n 2. paper \n 3. scissor \n") 
      
    # take the input from user 
    choice = int(input("User 1 turn: "))
    choice2 = int(input("User 2 turn: "))
  

       
    while (choice and choice2) > 3 or (choice and choice2) < 1: 
        choice = int(input("enter valid input: ")) 
        choice2 = int(input("enter valid input: ")) 
          
  

    if choice == 1: 
        choice_name = 'Rock'
    elif choice == 2: 
        choice_name = 'paper'
    else: 
        choice_name = 'scissor'
    
    if choice2 == 1: 
        choice_name2 = 'Rock'
    elif choice2 == 2: 
        choice_name2 = 'paper'
    else: 
        choice_name2 = 'scissor'
    
    
    print(choice_name) 
    print(choice_name2)
    
    if choice == choice2:
        print("Draw")
    
    new_choice1 = choice%(random.randint(1, 3))
    new_choice2 = choice % (random.randint(1, 3)) 
    
        if new_choice1 == new_choice2:
        print("Draw")

    if((new_choice1 == 1 and new_choice2 == 2) or
      (new_choice1 == 2 and new_choice2 ==1 )): 
        print("  paper wins  ", end = "") 
        result = "paper"
          
    elif((new_choice1 == 1 and new_choice2 == 0) or
        (new_choice1 == 0 and new_choice2 == 1)): 
        print("   Rock Wins    ", end = "") 
        result = "Rock"
    else: 
        print("   Scissor Wins    ", end = "") 
        result = "scissor"
    
    if result == choice_name:
        print(" You wins      ") 
    else: 
        print("      Computer wins ") 
