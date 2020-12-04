import random
roll = 0
count = 0

while roll!=5:
    roll = random.randint(1,5)
    count += 1
    print(roll)

print(f'it took {count} times to roll a 5')