#Nested if / else Explanation 
print ("Welcome to the rollercoaster!")

height = int(input("What is your height in cm? "))


if height >= 120:
    print("You can ride the rollercoaster! Yea!!!!")
    age = int(input("How old are you? "))
    if age < 12:
        print("You have to pay $5.00")
    elif age >= 12 and age <18:
        print("You have to pay $7.00")
    else:
        print("You have to pay $12.00")

else:
    print("You cant ride the rollercoaster :c")
