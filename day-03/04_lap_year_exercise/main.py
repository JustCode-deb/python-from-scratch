# Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February.

current_year = int(input("Please input a year number: "))

if current_year % 4 == 0:
    if current_year % 100 == 0:
        if current_year % 400:
            print("Leap")
        else:
            print("No Leap")
    else:
        print("Leap")
else:
    print("Not Leap")          