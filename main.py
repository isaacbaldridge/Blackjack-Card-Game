import random
class Deck:
    def __init__(self):
        # attributes are data that the class uses (here, it is cards, suits, and ranks seen below.)
        self.cards = []
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
                self.cards.append([suit, rank])

# methods are functions that a class executes using the attributes (data) in that class.
# here, it is the shuffle and deal functions.

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, number):
        cardsDealt = []
        for num in range(number):
            if len(self.cards) > 0:
                card = self.cards.pop()
                cardsDealt.append(card)
        return cardsDealt
    
deck1 = Deck()
deck2 = Deck()
deck2.shuffle()
print(deck1.cards)
print("---------------------------------")
print(deck2.cards)





















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