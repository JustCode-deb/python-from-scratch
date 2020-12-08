print("\t\t\t TIP calculator.\n\n\n")

total_bill = float(input("What was the total bill? "))

percent = float(input("\nWhat percentage tip you like to give? 10, 12 or 15? "))

pople = int(input("\n How many people to split the bill? "))

percentf = percent / 100 

extra = total_bill * percentf

result = ((total_bill + extra) / pople)
resultf = round(result,2)
print(f"Each person should pay: ${resultf}")