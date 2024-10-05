from typing import List
from .card import Card

class Player:
    """
    Represents a player in the card game.

    This class manages a player's hand of cards and provides methods for
    playing cards and receiving new ones.

    Attributes:
        name (str): The name of the player.
        hand (List[Card]): A list of Card objects representing the player's current hand.
    """

    def __init__(self, name: str):
        """
        Initialize a new player.

        Args:
            name (str): The name of the player.
        """
        self.name = name
        self.hand: List[Card] = []

    def play_card(self) -> Card:
        """
        Play a card from the player's hand.

        Returns:
            Card: The card played from the top of the player's hand.

        Raises:
            ValueError: If the player has no cards left in their hand.
        """
        if not self.hand:
            raise ValueError(f"{self.name} has no cards left to play.")
        return self.hand.pop(0)

    def receive_cards(self, cards: List[Card]) -> None:
        """
        Add cards to the player's hand.

        Args:
            cards (List[Card]): A list of Card objects to be added to the player's hand.
        """
        self.hand.extend(cards)

    def get_hand_size(self) -> int:
        """
        Get the number of cards in the player's hand.

        Returns:
            int: The number of cards in the player's hand.
        """
        return len(self.hand)

    def has_cards(self) -> bool:
        """
        Check if the player has any cards left.

        Returns:
            bool: True if the player has cards, False otherwise.
        """
        return len(self.hand) > 0

    def __str__(self) -> str:
        """
        Get a string representation of the player.

        Returns:
            str: A string describing the player and the number of cards in their hand.
        """
        return f"{self.name} ({self.get_hand_size()} cards)"

    def display_card(self) -> None:
        """
        Display the top card of the player's hand.

        This method is a placeholder for potential GUI integration.
        In a graphical implementation, this method would update the
        display to show the player's current card.
        """
        # This method would be implemented in a GUI version of the game
        pass