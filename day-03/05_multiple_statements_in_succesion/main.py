print ("Welcome to the rollercoaster!")

height = int(input("What is your height in cm? "))

total_bill = 0

if height >= 120:
    print("You can ride the rollercoaster! Yea!!!!")
    age = int(input("How old are you? "))
    if age < 12:
        bill = 5
    elif age >= 12 and age <18:
        bill = 5
    else:
        bill = 5
else:
    print("You cant ride the rollercoaster :c")

photo_query = input("Doy you want a photo taken? Y or N")
if photo_query == "Y":
    bill += 3
print(f"You have to pay {bill} ")
