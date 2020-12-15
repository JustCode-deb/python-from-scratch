#You are going to write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
import random

print("\t\t\tWho Pay The Bill")

names_input = input("Please fill this field with the name of the persons separated with a , :\n")

name = names_input.split(", ")
long_of_list = len(name)
random_pick = (random.randint(0,long_of_list -1))
print("****************************************************")
print(name[random_pick],"is going to buy the meal today!")
print("****************************************************")
