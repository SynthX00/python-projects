# numValue = '7'
# print(numValue.isnumeric())
# 
# strValue = 'Daniel'
# print(strValue.isnumeric())

firstNum = input("First number: ")
if not firstNum.isnumeric():
    print('Value is not a number. Retry')
    exit()

secondNum = input("Second number: ")
if not secondNum.isnumeric():
    print('Value is not a number. Retry')
    exit()

sum = int(firstNum) + int(secondNum)
print("Sum: " + str(sum))