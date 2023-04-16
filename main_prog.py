from random import randint
from time import sleep
from os import name , system

def clear():
   """clear terminal or cmd window"""
   # for windows
   if name == 'nt':
        system('cls')

   # for mac and linux
   else:
    system('clear')

def intro():
    """show intro before game start"""
    print("welcome to rock paper scissors game")
    sleep(2)

    clear()
    pass


def check(p , c):
    """check who win"""

    val = ["rock" , "paper" , "scissors"] #available choices
    print(f'player choice is : {val[p]} --> {p} \ncpu choice is : {val[c-3]} --> {c}') #print choices
    
    res = abs(p-c)

    #to understand conditions see excel file
    if res == 3 :
        print("tie")

    elif res in (5,2):
        print("winner is you !!")
        
    elif res in (4,1):
        print("winner is cpu !!")


#main 
intro()
for i in range(10):


    player_choice = int(input("enter number (0 , 1 , 2) : "))

    cpu_choice = randint(3,5)

    check(player_choice , cpu_choice)