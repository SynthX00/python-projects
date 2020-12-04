print("Would you like to continue?")
answer = input()

if answer == "no" or answer == "n":
    print("Exiting")
elif answer == "yes" or answer == "y":
    print("Continuing ...")
    print("Complete!")
else:
    print("Please try to answer with yes or no.")