#know the life of a person in weeks remaining if we life 90 years for this exercise

user_current_age = int(input("How old are you? "))

years_remaining = 90 - user_current_age

#Transform year to weeks
user_current_weeks =  (52 * years_remaining)

#Get user Days
user_current_days = (365 * years_remaining)

#Get user Months
user_current_months = (12 * years_remaining)

print(f"You have {user_current_days} days, {user_current_weeks} weeks and {user_current_months} months left")