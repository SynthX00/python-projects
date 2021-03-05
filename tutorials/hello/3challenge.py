print("Todays date?")
date = input()

print("Breakfast calories?")
breakfast = int(input())

print("Lunch calories?")
lunch = int(input())

print("Dinner calories?")
dinner = int(input())

print("Snack calories?")
snack = int(input())

totalcals = breakfast + lunch + dinner + snack
print("Your total calorie intake for " + date + " is: " + str(totalcals))
