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
    
def take_input():
    while True :

        player_choice = int(input("enter number (0 , 1 , 2) : "))
        
        if player_choice not in (0,1,2) :
            print("incorrect input /\ try again .")
        else :
            break
    cpu_choice = randint(3,5)

    return (player_choice , cpu_choice)

def check(p , c):
    """check who win"""

    clear()
    val = ["rock" , "paper" , "scissors"] #available choices
    print(f'player choice is : {val[p]} --> {p} \ncpu choice is : {val[c-3]} --> {c}\n\n') #print choices
    sleep(1)
    res = abs(p-c)

    #to understand conditions see excel file
    if res == 3 :
        print("tie")

    elif res in (5,2):
        print("winner is you !!")
        
    elif res in (4,1):
        print("winner is cpu !!")

    print("\n\nnext round ...")
    sleep(2.5)
    clear()

#main 
intro()
for i in range(10):

    p_c_choice = take_input()

    check(p_c_choice[0] , p_c_choice[1] )