# src/card.py

class Card:
    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    def __init__(self, rank, suit):
        if rank not in self.RANKS:
            raise ValueError(f"Invalid rank: {rank}")
        if suit not in self.SUITS:
            raise ValueError(f"Invalid suit: {suit}")
        self.rank = rank
        self.suit = suit
        self.facedown = False

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def get_value(self):
        return self.RANKS.index(self.rank)

    def __lt__(self, other):
        return self.get_value() < other.get_value()

    def __gt__(self, other):
        return self.get_value() > other.get_value()

    def __eq__(self, other):
        return self.get_value() == other.get_value()