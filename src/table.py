# src/table.py

class Table:
    def __init__(self):
        self.played_cards = {}

    def place_card(self, player, card):
        self.played_cards[player.name] = card  # Use player.name as the key

    def clear(self):
        self.played_cards.clear()

    def get_winner(self):
        if not self.played_cards:
            return None
        return max(self.played_cards, key=lambda p: self.played_cards[p])

    def collect_cards(self):
        cards = list(self.played_cards.values())
        self.clear()
        return cards