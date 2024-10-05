import random
from .card import Card

class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in Card.SUITS for rank in Card.RANKS]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num_players=2):
        if num_players < 2:
            raise ValueError("At least two players are required.")
        
        cards_per_player = len(self.cards) // num_players
        hands = [[] for _ in range(num_players)]
        
        for i in range(cards_per_player * num_players):
            hands[i % num_players].append(self.cards[i])
        
        return hands

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        return f"Deck of {len(self)} cards"