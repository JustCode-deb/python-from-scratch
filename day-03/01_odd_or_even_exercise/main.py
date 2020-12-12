#Detect Odd or Even Number with conditions

numer_1 = float(input("Please type your first number: ")) 
numer_2 = float(input("Please type your first number: ")) 

#Evaluation
answ = numer_1 % numer_2

if answ == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")