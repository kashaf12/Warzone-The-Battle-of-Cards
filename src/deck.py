import random
from typing import List
from .card import Card

class Deck:
    """
    Represents a deck of playing cards.

    This class manages a collection of Card objects, provides methods for
    shuffling the deck, and dealing cards to players.

    Attributes:
        cards (List[Card]): A list containing all the Card objects in the deck.
    """

    def __init__(self):
        """
        Initialize a new deck of cards.

        Creates a standard 52-card deck with all combinations of ranks and suits.
        """
        self.cards = [Card(rank, suit) for suit in Card.SUITS for rank in Card.RANKS]

    def shuffle(self) -> None:
        """
        Shuffle the deck of cards.

        This method randomizes the order of cards in the deck.
        """
        random.shuffle(self.cards)

    def deal(self, num_players: int) -> List[List[Card]]:
        """
        Deal cards to a specified number of players.

        Args:
            num_players (int): The number of players to deal cards to.

        Returns:
            List[List[Card]]: A list of hands, where each hand is a list of Card objects.

        Raises:
            ValueError: If the number of players is less than 2 or if there aren't enough cards to deal.
        """
        if num_players < 2:
            raise ValueError("At least two players are required.")
        
        cards_per_player = len(self.cards) // num_players
        if cards_per_player == 0:
            raise ValueError("Not enough cards to deal to all players.")

        hands = [[] for _ in range(num_players)]
        
        for i in range(cards_per_player * num_players):
            hands[i % num_players].append(self.cards[i])
        
        return hands

    def __len__(self) -> int:
        """
        Get the number of cards remaining in the deck.

        Returns:
            int: The number of cards in the deck.
        """
        return len(self.cards)

    def __str__(self) -> str:
        """
        Get a string representation of the deck.

        Returns:
            str: A string describing the number of cards in the deck.
        """
        return f"Deck of {len(self)} cards"