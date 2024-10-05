# src/game.py

from .deck import Deck
from .player import Player
from .table import Table

class Game:
    def __init__(self, player1_name, player2_name):
        self.deck = Deck()
        self.players = [Player(player1_name), Player(player2_name)]
        self.table = Table()

    def shuffle(self):
        self.deck.shuffle()

    def deal(self):
        hands = self.deck.deal(len(self.players))
        for player, hand in zip(self.players, hands):
            player.receive_cards(hand)

    def play_round(self):
        if not all(player.has_cards() for player in self.players):
            return self.get_winner()

        self.table.clear()  # Clear the table before playing new cards
        for player in self.players:
            if player.has_cards():
                card = player.play_card()
                self.table.place_card(player, card)

        winner = self.get_round_winner()
        if winner:
            cards_won = self.table.collect_cards()
            winner.receive_cards(cards_won)

        return self.get_winner()

    def get_round_winner(self):
        if not self.table.played_cards:
            return None
        winning_card = max(self.table.played_cards.values(), key=lambda card: card.get_value())
        for player in self.players:
            if self.table.played_cards.get(player.name) == winning_card:
                return player
        return None

    def get_winner(self):
        return next((player for player in self.players if len(player.hand) == 52), None)

    def is_game_over(self):
        return any(len(player.hand) == 52 for player in self.players)