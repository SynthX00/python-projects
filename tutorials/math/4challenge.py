print("Simple Calculator!")

first = input("First Value: ")
if first.isnumeric() == False:
    exit()

operator = input("Operation (+ - * / % **): ")
if operator.isalpha == False:
    exit()
float(first)

second = input("Second Value: ")
if second.isnumeric() == False:
    exit()
float(second)

total = 0
if operator == '+':
    total = first + second
elif operator == '-':
    total = first - second
elif operator == '*':
    total = first * second
elif operator == '/':
    total = first / second
elif operator == '**':
    total = first ** second
elif operator == '%':
    total = first % second
else:
    exit()

print("Result: " + str(round(total,2)))