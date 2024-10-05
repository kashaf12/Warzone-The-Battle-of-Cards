from typing import Dict, List, Optional
from .player import Player
from .card import Card

class Table:
    """
    Represents the game table in the card game.

    This class manages the cards played in each round, determines the winner
    of each round, and handles the collection of played cards.

    Attributes:
        played_cards (Dict[str, Card]): A dictionary mapping player names to their played cards.
    """

    def __init__(self):
        """
        Initialize a new game table.
        """
        self.played_cards: Dict[str, Card] = {}

    def place_card(self, player: Player, card: Card) -> None:
        """
        Place a card on the table for a specific player.

        Args:
            player (Player): The player placing the card.
            card (Card): The card being placed on the table.
        """
        self.played_cards[player.name] = card

    def clear(self) -> None:
        """
        Clear all cards from the table.
        """
        self.played_cards.clear()

    def get_round_winner(self) -> Optional[str]:
        """
        Determine the winner of the current round.

        Returns:
            Optional[str]: The name of the winning player, or None if it's a tie.
        """
        if not self.played_cards:
            return None

        max_card = max(self.played_cards.values())
        winners = [player for player, card in self.played_cards.items() if card == max_card]

        return winners[0] if len(winners) == 1 else None

    def collect_cards(self) -> List[Card]:
        """
        Collect all cards from the table.

        Returns:
            List[Card]: A list of all cards that were on the table.
        """
        cards = list(self.played_cards.values())
        self.clear()
        return cards

    def display_played_cards(self) -> None:
        """
        Display the cards currently on the table.

        This method is a placeholder for potential GUI integration.
        In a graphical implementation, this method would update the
        display to show all cards currently on the table.
        """
        # This method would be implemented in a GUI version of the game
        pass

    def __str__(self) -> str:
        """
        Get a string representation of the table.

        Returns:
            str: A string describing the cards currently on the table.
        """
        return " | ".join(f"{player}: {card}" for player, card in self.played_cards.items())