#Build a rock, paper or scissor game🎲🎲🎲🎲🎲🎲

import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("This is a Rock, Paper or Scissors game")
user_choose = input("What do you chose? ")

user_choose_correct = user_choose.lower()

#Computer ramdom
pc_random_generated = random.randint(1,3)
if pc_random_generated == 1:
    pc_choose = "rock"
elif pc_random_generated == 2:
    pc_choose = "paper"
elif pc_random_generated == 3:
    pc_choose = "scissors"
else:
    print("The computer fail, LOL")
#****************

if user_choose_correct == "rock" and pc_choose == "rock":
    print("Your Chose\n")
    print(rock)
    print("\nComputer Chose\n")
    print(rock)
    print("\nTie")
elif user_choose_correct == "paper" and pc_choose == "paper":
    print("Your Chose\n")
    print(paper)
    print("\nComputer Chose\n")
    print(paper)
    print("\nTie")
elif user_choose_correct == "scissors" and pc_choose == "scissors":
    print("Your Chose\n")
    print(scissors)
    print("\nComputer Chose\n")
    print(scissors)
    print("\nTie")
#*****************
elif user_choose_correct == "rock" and pc_choose == "paper":
    print("Your Chose\n")
    print(rock)
    print("\nComputer Chose\n")
    print(paper)
    print("\nPc Wins")
elif user_choose_correct == "rock" and pc_choose == "scissors":
    print("Your Chose\n")
    print(rock)
    print("\nComputer Chose\n")
    print(scissors)
    print("\nYou Wins")
#*****************
elif user_choose_correct == "paper" and pc_choose == "rock":
    print("Your Chose\n")
    print(paper)
    print("\nComputer Chose\n")
    print(rock)
    print("\nYou Wins")
elif user_choose_correct == "paper" and pc_choose == "scissors":
    print("Your Chose\n")
    print(paper)
    print("\nComputer Chose\n")
    print(scissors)
    print("\nPc Wins") 
#*****************
elif user_choose_correct == "scissors" and pc_choose == "rock":
    print("Your Chose\n")
    print(scissors)
    print("\nComputer Chose\n")
    print(rock)
    print("\nPc Wins") 
elif user_choose_correct == "scissors" and pc_choose == "paper":
    print("Your Chose\n")
    print(scissors)
    print("\nComputer Chose\n")
    print(paper)
    print("\nYou Wins")

