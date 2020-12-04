import random

ranks = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
suits = ['Hearts','Spades','Clubs','Diamonds']
deck = []

for suit in suits:
    for rank in ranks:
        deck.append(f'{rank} of {suit}')

print(f'There are {len(deck)} cards in the deck.')

hand = []
print('Dealing cards...')

for i in range(5):
    card = random.choice(deck)
    hand.append(card)
    deck.remove(card)

print(f'There are {len(deck)} cards in the deck.')
print(hand)