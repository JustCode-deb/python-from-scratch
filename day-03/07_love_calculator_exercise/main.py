#Love Calculator

name_1 = input("What is your name? ")
name_2 = input("What is their name? ")

name_1 = name_1.lower()
name_2 = name_2.lower()

t = name_1.count("t")
r = name_1.count("r")
u = name_1.count("u")
e = name_1.count("e")
l = name_2.count("l")
o = name_2.count("o")
v = name_2.count("v")
e = name_2.count("e")

your_number = t+r+u+e
their_number = l+o+v+e

score = int(str(your_number) + str(their_number))

if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
