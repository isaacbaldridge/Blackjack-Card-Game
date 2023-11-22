import random
cards = []
suits = ["spades", "clubs", "hearts", "diamonds"]
ranks = [
    {"rank": "A", "value": 11},
    {"rank": "2", "value": 2},
    {"rank": "3", "value": 3},
    {"rank": "4", "value": 4},
    {"rank": "5", "value": 5},
    {"rank": "6", "value": 6},
    {"rank": "7", "value": 7},
    {"rank": "8", "value": 8},
    {"rank": "9", "value": 9},
    {"rank": "10", "value": 10},
    {"rank": "J", "value": 10},
    {"rank": "Q", "value": 10},
    {"rank": "K", "value": 10}
]

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

card = deal(1)[0]

print(card[1]["value"])




















# cardsDealt = deal(2)
# print(cardsDealt)
# card = cardsDealt[0]
# rank = card[1]

# if rank == "A":
#     value = 11
# elif rank == "J" or rank == "Q" or rank == "K":
#     value = 10
# else:
#     value = rank
    
# print(card)

# rank_dict = {
#     "rank": rank,
#     "value": value 
# }

# print(rank_dict["rank"], rank_dict["value"])