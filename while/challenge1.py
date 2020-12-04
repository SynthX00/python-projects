import random
import emoji

numberToGuess = random.randint(1,10)
guess = 0
count = 0


print('Guess a number between 1 and 10')
while guess != numberToGuess:
    
    count+=1
    value = input(f'Enter guess #{count}: ')
    if(not value.isnumeric()):
        print('input is invalid, try again')
        continue

    guess = int(value)
    if(guess>numberToGuess):
        print('Your guess is too high, try again!')
    elif(guess<numberToGuess):
        print('Your guess is too low, try again!')

msg = emoji.emojize(':face_with_tears_of_joy:')
print(f'you made the right guess! you "only" took {count} tries {msg}')