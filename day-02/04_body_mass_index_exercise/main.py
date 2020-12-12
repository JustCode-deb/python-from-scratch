#Body Mass Index Calculator 

print("\t\tBody Mass Index Calculator\n\n")

height = float(input("Plese insert your height: "))
weight = float(input("Please insert your weight: "))

bmi = (weight / (height ** 2))


print(int(bmi))