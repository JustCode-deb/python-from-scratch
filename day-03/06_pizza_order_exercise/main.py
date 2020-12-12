# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

# Based on a user's order, work out their final bill.

print("\t\t\tBuild your Pizza \U0001F355\n\n")

bill = 0
more_peperoni_S = 2 
more_peperoni = 3
print("\t\t\t This our menu")
print("\t***********************************")
print("Small Pizza: $15.00\n")
print("Medium Pizza: $20.00\n")
print("Large Pizza: $25.00\n\n")
print("\t***********************************")

answer_size = input("Please chone one: S, M, L: ")

if answer_size == "S":
    bill = 15
    answer = input("Do you want extra peperoni for you pizza for $2.00? ")
    if answer == "Y":
        bill += more_peperoni_S
elif answer_size == "M":
    bill = 20
    answer = input("Do you want extra peperoni for you pizza for $3.00? ")
    if answer == "Y":
        bill += more_peperoni
elif answer_size == "L":
    bill = 25
    answer = input("Do you want extra peperoni for you pizza for $3.00? ")
    if answer == "Y":
        bill += more_peperoni
else:
    print("Invalid input")

answer_cheese = input("Do you want extra cheese in your pizza for $1.00?")
if answer_cheese == "Y":
    bill += 1

print(f"Your final bill is {bill}")
