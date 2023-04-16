from random import randint
from time import sleep
from os import name , system

last_win = ["" , 0] #player name to win streak (two value available "player" and "cpu")

player_point = 0
cpu_point = 0

winner = ""


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

def win_check():
    global winner
    if last_win[1] == 5 :
        winner = last_win[0]

def addpoint(who):
    global player_point , cpu_point
    if who == last_win[0] :
        last_win[1] += 1
        
    else :
        last_win[0] = who
        last_win[1] = 1

    if who == "player" :
        player_point += (2 ** (last_win[1]-1))

    else :
        cpu_point += (2 ** (last_win[1]-1))

    win_check()
    
def show_point() :
    print(f"player poin --> {player_point} \t\t\tcpu point --> {cpu_point}\t\tlast win : {last_win[0]} --> {last_win[1]} \n\n")

def take_input():
    show_point()
    while True :
        player_choice = int(input("enter number (0 : rock , 1 :paper , 2 : scissors ) : "))
        
        if player_choice not in (0,1,2) :
            print("incorrect input /\ try again .")
        else :
            break

    cpu_choice = randint(3,5)
    return (player_choice , cpu_choice)

def check(p , c):
    """check who win"""

    clear()
    show_point()
    val = ["rock" , "paper" , "scissors"] #available choices
    print(f'player choice is : {val[p]} \ncpu choice is : {val[c-3]}\n\n') #print choices
    sleep(1)
    res = abs(p-c)

    #to understand conditions see excel file
    if res == 3 :
        print("tie")

    elif res in (5,2):
        addpoint("player")
        print(f"winner is you !! your point plus {2 ** (last_win[1]-1)}")
    elif res in (4,1):
        addpoint("cpu")
        print(f"winner is cpu !! cpu point plus {2 ** (last_win[1]-1)}")

    print("\n\nnext round ...")
    sleep(2.5)
    clear()

def end_match():
    return True if input(f"match end. \nwinner is {winner}\nplayagain (y,n)?") == "y" else False

def restart():
    global player_point , cpu_point , winner , last_win
    last_win = ["" , 0]

    player_point = cpu_point = 0

    winner = ""
    clear()


#main 
intro()
while True :
    while (abs(player_point-cpu_point) < 50) and (not winner) :

        p_c_choice = take_input()

        check(p_c_choice[0] , p_c_choice[1] )

    if end_match():
        restart()
    else:
        break