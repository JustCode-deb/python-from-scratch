# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

# It should tell them the interpretation of their BMI based on the BMI value.

# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.


print("\t\tBody Mass Index Calculator\n\n")

height = float(input("Plese insert your height: "))
weight = float(input("Please insert your weight: "))

bmi = (weight / (height ** 2))


print(int(bmi))

if bmi <= 18.5:
    print("Your are underweight")
elif bmi > 18.5 and bmi <= 25:
    print("You are on normal weight")
elif bmi > 25 and bmi <= 30:
    print("You are slightly overweight")
elif bmi > 30 and bmi <= 35:
    print("Your are obese")
else:
    print("Your are clinically obese")
