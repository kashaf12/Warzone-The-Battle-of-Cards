from typing import Optional, List
from .deck import Deck
from .player import Player
from .table import Table
from .rules import Rules
from .card import Card

class Game:
    """
    Represents the main game logic for Warzone: The Battle of Cards.

    This class manages the overall game state, including players, the deck,
    the table, and game rules. It provides methods for game setup and gameplay.

    Attributes:
        deck (Deck): The deck of cards used in the game.
        players (List[Player]): The list of players in the game.
        table (Table): The game table where cards are played.
        rules (Rules): The set of rules governing the game.
    """

    def __init__(self, player1_name: str, player2_name: str, rules: Rules):
        """
        Initialize a new game.

        Args:
            player1_name (str): The name of the first player.
            player2_name (str): The name of the second player.
            rules (Rules): The rule set for the game.
        """
        self.rules = rules
        self.deck = Deck()
        if self.rules.use_double_deck:
            self.deck.cards.extend(Deck().cards)  # Add a second deck
        self.players = [Player(player1_name), Player(player2_name)]
        self.table = Table()

    def shuffle(self) -> None:
        """
        Shuffle the deck of cards.
        """
        self.deck.shuffle()

    def deal(self) -> None:
        """
        Deal cards to all players.
        """
        hands = self.deck.deal(len(self.players))
        for player, hand in zip(self.players, hands):
            player.receive_cards(hand)

    def play_round(self) -> Optional[Player]:
        """
        Play a single round of the game.

        Returns:
            Optional[Player]: The winner of the game if the game ends, otherwise None.
        """
        if not all(player.has_cards() for player in self.players):
            return self.get_winner()

        self.table.clear()
        for player in self.players:
            if player.has_cards():
                card = player.play_card()
                self.table.place_card(player, card)

        winner_name = self.table.get_round_winner()
        if winner_name:
            winner = next(player for player in self.players if player.name == winner_name)
            winner.receive_cards(self.table.collect_cards())
        else:
            self._resolve_war()

        return self.get_winner()

    def _resolve_war(self) -> None:
        """
        Resolve a war situation.
        """
        war_players = self.players.copy()
        war_cards: List[Card] = []

        while len(set(card.get_value() for card in self.table.played_cards.values())) == 1:
            # Check if any player ran out of cards
            war_players = [p for p in war_players if p.has_cards()]
            if len(war_players) == 1:
                war_players[0].receive_cards(self.table.collect_cards() + war_cards)
                return

            # Each player puts down face-down cards
            for player in war_players:
                if player.has_cards():
                    war_cards.append(player.play_card())

            # Each player puts down a face-up card
            self.table.clear()
            for player in war_players:
                if player.has_cards():
                    card = player.play_card()
                    self.table.place_card(player, card)
                    war_cards.append(card)

        # Determine war winner
        winner_name = self.table.get_round_winner()
        if winner_name:
            winner = next(player for player in self.players if player.name == winner_name)
            winner.receive_cards(self.table.collect_cards() + war_cards)

    def get_winner(self) -> Optional[Player]:
        """
        Get the winner of the game.

        Returns:
            Optional[Player]: The player who has won the game, or None if the game is not over.
        """
        for player in self.players:
            if len(player.hand) == len(self.deck.cards):
                return player
        return None

    def is_game_over(self) -> bool:
        """
        Check if the game is over.

        Returns:
            bool: True if the game is over, False otherwise.
        """
        return any(len(player.hand) == len(self.deck.cards) for player in self.players)

    def __str__(self) -> str:
        """
        Get a string representation of the current game state.

        Returns:
            str: A string describing the current state of the game.
        """
        return (f"Game State:\n"
                f"Players: {', '.join(str(player) for player in self.players)}\n"
                f"Table: {self.table}\n"
                f"Rules: {self.rules}")
    

    