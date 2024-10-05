
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def play_card(self):
        if not self.hand:
            raise ValueError("No cards left in hand")
        return self.hand.pop(0)

    def receive_cards(self, cards):
        self.hand.extend(cards)

    def __str__(self):
        return f"{self.name} ({len(self.hand)} cards)"

    def has_cards(self):
        return len(self.hand) > 0