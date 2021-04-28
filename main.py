# Rock Paper Scissors with some actual difficulty, as the computer will use stats
# To try and win against you

from time import sleep
from os import system
from random import random

#######################################
# These grids are what people would pick AFTER picking the given
# Choices (R, P, S)
chances_1 = [ # After the first turn
    [0.445, 0.354, 0.201], # R {R P S}
    [0.288, 0.421, 0.292], # P {R P S}
    [0.176, 0.308, 0.516]] # S {R P S}
#
chances_2 = [ # After 2 turns
    [0.684, 0.201, 0.115], # R R {R P S}
    [0.226, 0.325, 0.449], # R P
    [0.185, 0.618, 0.197], # R S
    [0.238, 0.381, 0.381], # P R
    [0.212, 0.590, 0.198], # P P
    [0.357, 0.330, 0.313], # P S
    [0.241, 0.648, 0.111], # S R
    [0.455, 0.292, 0.253], # S P 
    [0.075, 0.183, 0.742]] # S S
#
prev_turns = ["rr", "rp", "rs", "pr", "pp", "ps", "sr", "sp", "ss"] # Will be used to determine which row of the chances_2 table is used
#######################################

def turn1():
    return "p" # Ignore this function it is very amazing and I love it :))))

def turn2(choice):
    choice = choice.lower()
    if(choice.startswith("r")):
        row = 0
    elif(choice.startswith("p")):
        row = 1
    else:
        row = 2
    num1 = chances_1[row][0]
    num2 = chances_1[row][1] + num1
    num3 = chances_1[row][2] + num2
    random_number = round(random(), 5)
    if(random_number < num1):
        return "p"
    elif(num1 < random_number < num2):
        return "s"
    else:
        return "r"

def other_turn(combo):
    for i in range(0, 9):
        if(combo == prev_turns[i]):
            row = i
    num1 = chances_2[row][0]
    num2 = chances_2[row][1] + num1
    num3 = chances_2[row][2] + num2
    random_number = round(random(), 5)
    if(random_number < num1):
        return "p"
    elif(num1 < random_number < num2):
        return "s"
    else:
        return "r"


def check_for_winner(user, computer):
    user = user[0]
    if(user == "r" and computer == "s") or (user == "p" and computer == "r") or (user == "s" and computer == "p"):
        return "you"
    elif(user == "r" and computer == "p") or (user == "p" and computer == "s") or (user == "s" and computer == "r"):
        return "computer"
    else:
        return "tie"

def game():
    turn = 1
    user_choices = []
    score = [0, 0]
    print("Rock Paper Scissors with statistical analysis.")
    sleep(2)
    while(1):
        system("CLS")
        user_input = input("Enter your choice rock / paper / scissors!\n")
        user_choices.append(user_input)
        if(user_input == ""):
            user_input = "r"
        if(turn == 1):
            computer_input = turn1()
        elif(turn == 2):
            computer_input = turn2(user_choices[0])
        else:
            previous_choices = user_choices[-2:-1][0].lower() + user_choices[-1:][0].lower()
            computer_input = other_turn(previous_choices)
        winner = check_for_winner(user_input, computer_input)
        print("The computer chose " + computer_input + " you chose " + user_input + " therefore...")
        if(winner == "you"):
            score[0] += 1
        elif(winner == "computer"):
            score[1] += 1
        if(winner != "tie"):
            print("The winner is... " + winner + "!")
        else:
            print("It is a tie!")
        print("The turn is...", turn)
        print("The score is:", score[0], "to", score[1])
        turn += 1
        sleep(4)

game()
