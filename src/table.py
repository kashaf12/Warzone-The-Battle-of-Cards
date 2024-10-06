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
        self.last_played_cards: Dict[str, Card] = {} 

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
        self.last_played_cards = self.played_cards.copy()  # Store the last played cards
        self.played_cards.clear()  # Clear for the next round

    def get_round_winner(self) -> Optional[str]:
        cards_to_check = self.played_cards if self.played_cards else self.last_played_cards
        if not cards_to_check:
            return None
        max_card = max(cards_to_check.values(), key=lambda card: card.get_value())
        winners = [player for player, card in cards_to_check.items() if card.get_value() == max_card.get_value()]
        return winners[0] if len(winners) == 1 else None
    
    def collect_cards(self) -> List[Card]:
        cards = list(self.played_cards.values()) + list(self.last_played_cards.values())
        self.clear()
        return cards

    def display_played_cards(self) -> Dict[str, str]:
        """
        Prepare the played cards for display.

        Returns:
            Dict[str, str]: A dictionary mapping player names to string representations of their played cards.
        """
        return {player: str(card) for player, card in self.played_cards.items()}
    
    def __str__(self) -> str:
        """
        Get a string representation of the table.

        Returns:
            str: A string describing the cards currently on the table and the last round's winner.
        """
        current_round = " | ".join(f"{player}: {card}" for player, card in self.played_cards.items())
        return f"Current round: {current_round}"

    def __str__(self) -> str:
        """
        Get a string representation of the table.

        Returns:
            str: A string describing the cards currently on the table.
        """
        return " | ".join(f"{player}: {card}" for player, card in self.played_cards.items())