# This is treasure island day 3 of my 10 days of code challenge
# In this project the user goes through a series of questions to find the hidden
# treasure.

# Welcome statment and intro photo.
print('''
 _                                     _     _                 _
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|

''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# Ask the user to start the program
start_sequence = input("Enter start to begin!\n")

# If user enters start we start the game.
if start_sequence == "start":
    # first step in storyline ask for input from the user then change input to lower case.
    first_step = input('You\'ve come to a fork, where do you want to go? Type "left" or "right"\n')
    lower_first_step = first_step.lower()

# First level of the game.
    if lower_first_step == "left":
        second_step = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n')
        lower_second_step = second_step.lower()
    else:
        print("You were eaten by bees!")
        exit()

# Second level of the game.
    if lower_second_step == "wait":
        third_step = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n')
        lower_third_step = third_step.lower()
    else:
        print("You were sweept away by the currents, and eaten by piranahs")
        exit()

# Third level of the game.
    if lower_third_step == "yellow":
        print("You found the treasure! You Win!")
        print('''
        *******************************************************************************
                  |                   |                  |                     |
         _________|________________.=""_;=.______________|_____________________|_______
        |                   |  ,-"_,=""     `"=.|                  |
        |___________________|__"=._o`"-._        `"=.______________|___________________
                  |                `"=._o`"=._      _`"=._                     |
         _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
        |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
        |___________________|_._"  ,. .$ ` `` ,  `"-._"-._   ". '__|___________________
                  |           |o`"=._` , "` `$ .". ,  "-._"-._; ;              |
         _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
        |                   | |o;    `"-.o`"=._``  '` $ ,__.--o;   |
        |___________________|_| ;     ($) `-.o `"=.`_.--"_o.-; ;___|___________________
        ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
        /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
        ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
        /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
        ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
        /______/______/______/______/______/______/______/______/______/______/_____ /
        *******************************************************************************''')
    elif lower_third_step == "red":
        print("You were SUS and have been ejected!")
    else:
        print("You rolled your ankle stepping on a crack and broke your ma's back!")
