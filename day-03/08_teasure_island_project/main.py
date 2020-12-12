print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

question = input("You are in the island, you have 2 ways, left or right, choose one: ")

if question == "left":
    question = input("You see a river you have two options, swim or wait for a boat choose one: swim | wait ")
    if question == "wait":
        question = input("Now you can see 3 Doors select one: red, blue, yellow: ")
        if question == "red":
            print("You get burned by fire\n")
            print("GAME OVER!")
        elif question == "blue":
            print("You get eaten by beast\n")
            print("GAME OVER!")
        elif question == "yellow":
            print("YOU WIN!")
        else:
            print("WRONG ANSWER YOU LOST!")
    else:
        print("You get attak by trout!")
        print("GAME OVER!")
else:
    print("You fall into a hole ")
    print("GAME OVER!")