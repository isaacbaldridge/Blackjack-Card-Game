import random


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
# __str__ is called whenever a print function for an instance of the Card class is called.
    def __str__(self):
        return f"{self.rank['rank']} of {self.suit}"


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
                self.cards.append(Card(suit, rank))

# methods are functions that a class executes using the attributes (data) in that class.
# here, it is the shuffle and deal functions.
# the methods are not indented the same as attributes because they are not part of the init method.
# every defined function is a method (__init__, shuffle, and deal)
    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self, number):
        cardsDealt = []
        for num in range(number):
            if len(self.cards) > 0:
                card = self.cards.pop()
                cardsDealt.append(card)
        return cardsDealt
    
card1 = Card("hearts", {"rank": "J", "value": 10})
print(card1)























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