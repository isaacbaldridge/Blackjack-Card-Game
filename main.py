import random
cards = []
suits = ["spades", "clubs", "hearts", "diamonds"]
ranks = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

for suit in suits:
    for rank in ranks:
        # print([suit, rank])
        cards.append([suit, rank])


def shuffle():
    random.shuffle(cards)

def deal(number):
    cardsDealt = []
    for num in range(number):
        card = cards.pop()
        cardsDealt.append(card)
    return cardsDealt

shuffle()
cardsDealt = deal(2)
card = cardsDealt[0]
rank = card[1]

if rank == "A":
    value = 11
elif rank == "J" or rank == "Q" or rank == "K":
    value = 10
else:
    value = rank
    
# print(card)
print(rank, value)