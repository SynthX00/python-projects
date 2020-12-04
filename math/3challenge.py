fahrenheit = input("What's the temperature in Fahrenheit? ")
if fahrenheit.isnumeric() == False:
    print("Input must be numeric!")
    exit()

celsius = (float(fahrenheit) - 32) * 5/9

print("Temprature in Celsius is " + str(int(celsius)))