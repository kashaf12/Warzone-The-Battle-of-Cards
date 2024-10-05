from typing import Optional
from .player import Player
from .card import Card

class Rules:
    """
    Represents the rule set for the Warzone: The Battle of Cards game.

    This class encapsulates various game rules and provides methods for
    resolving special situations like wars and speed wars.

    Attributes:
        war_resolution_method (str): The method used to resolve wars ('standard', 'double', or 'quadruple').
        use_double_deck (bool): Whether the game uses a double deck (104 cards).
        speed_war_enabled (bool): Whether the speed war rule is enabled.
    """

    def __init__(self, war_resolution_method: str = 'standard', use_double_deck: bool = False, speed_war_enabled: bool = False):
        """
        Initialize a new rule set for the game.

        Args:
            war_resolution_method (str): The method for resolving wars. Default is 'standard'.
            use_double_deck (bool): Whether to use a double deck. Default is False.
            speed_war_enabled (bool): Whether to enable the speed war rule. Default is False.
        """
        self.war_resolution_method = war_resolution_method
        self.use_double_deck = use_double_deck
        self.speed_war_enabled = speed_war_enabled

    def resolve_war(self, player1: Player, player2: Player) -> Optional[Player]:
        """
        Resolve a war between two players.

        This method implements the war resolution based on the chosen method.

        Args:
            player1 (Player): The first player in the war.
            player2 (Player): The second player in the war.

        Returns:
            Optional[Player]: The winner of the war, or None if it's a tie or players run out of cards.
        """
        cards_to_play = 1  # Standard war

        if self.war_resolution_method == 'double':
            cards_to_play = 2
        elif self.war_resolution_method == 'quadruple':
            cards_to_play = 4

        # Check if players have enough cards for the war
        if player1.get_hand_size() < cards_to_play + 1 or player2.get_hand_size() < cards_to_play + 1:
            return player1 if player1.get_hand_size() > player2.get_hand_size() else player2

        # Play face-down cards
        face_down_cards = []
        for _ in range(cards_to_play):
            face_down_cards.extend([player1.play_card(), player2.play_card()])

        # Play face-up cards
        card1 = player1.play_card()
        card2 = player2.play_card()

        if card1 > card2:
            player1.receive_cards(face_down_cards + [card1, card2])
            return player1
        elif card2 > card1:
            player2.receive_cards(face_down_cards + [card1, card2])
            return player2
        else:
            # Another tie, recursively resolve
            return self.resolve_war(player1, player2)

    def is_speed_war(self, card1: Card, card2: Card) -> bool:
        """
        Determine if a speed war occurs between two cards.

        A speed war occurs when the two cards are exactly one rank apart.

        Args:
            card1 (Card): The first card to compare.
            card2 (Card): The second card to compare.

        Returns:
            bool: True if it's a speed war, False otherwise.
        """
        if not self.speed_war_enabled:
            return False

        rank_diff = abs(Card.RANKS.index(card1.rank) - Card.RANKS.index(card2.rank))
        return rank_diff == 1 or rank_diff == 12  # 12 for Ace-King adjacency

    def __str__(self) -> str:
        """
        Get a string representation of the current rule set.

        Returns:
            str: A string describing the current game rules.
        """
        return (f"War Resolution: {self.war_resolution_method.capitalize()}, "
                f"Double Deck: {'Yes' if self.use_double_deck else 'No'}, "
                f"Speed War: {'Enabled' if self.speed_war_enabled else 'Disabled'}")