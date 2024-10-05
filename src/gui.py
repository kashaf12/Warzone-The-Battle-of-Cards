import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from typing import Dict, Optional
from .game import Game
from .rules import Rules

class GUI:
    """
    Graphical User Interface for Warzone: The Battle of Cards.

    This class creates and manages the game's visual interface using Tkinter.
    It handles user interactions and updates the display based on the game state.

    Attributes:
        game (Game): The main game logic instance.
        root (tk.Tk): The main window of the application.
        card_images (Dict[str, ImageTk.PhotoImage]): Dictionary of card images.
    """

    def __init__(self, game: Game):
        """
        Initialize the GUI.

        Args:
            game (Game): The main game logic instance.
        """
        self.game = game
        self.root = tk.Tk()
        self.root.title("Warzone: The Battle of Cards")
        self.root.geometry("800x600")

        self.card_images = self.load_card_images()

        self.create_widgets()

    def load_card_images(self) -> Dict[str, ImageTk.PhotoImage]:
        """
        Load card images from files.

        Returns:
            Dict[str, ImageTk.PhotoImage]: A dictionary of card images.
        """
        images = {}
        # Implementation details for loading images...
        return images

    def create_widgets(self):
        """Create and arrange all widgets in the GUI."""
        # Top row (larger)
        top_frame = tk.Frame(self.root)
        top_frame.pack(expand=True, fill=tk.BOTH)

        # Player 1 frame (left)
        self.player1_frame = tk.Frame(top_frame, width=400)
        self.player1_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.player1_label = tk.Label(self.player1_frame, text="Player 1 - Remaining Cards: 26")
        self.player1_label.pack(pady=10)
        self.player1_card = tk.Label(self.player1_frame)
        self.player1_card.pack(expand=True)

        # Player 2 frame (right)
        self.player2_frame = tk.Frame(top_frame, width=400)
        self.player2_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)
        self.player2_label = tk.Label(self.player2_frame, text="Player 2 - Remaining Cards: 26")
        self.player2_label.pack(pady=10)
        self.player2_card = tk.Label(self.player2_frame)
        self.player2_card.pack(expand=True)

        # Bottom row (smaller)
        bottom_frame = tk.Frame(self.root)
        bottom_frame.pack(fill=tk.X)

        # Buttons frame (left side of bottom row)
        buttons_frame = tk.Frame(bottom_frame)
        buttons_frame.pack(side=tk.LEFT, expand=True)

        self.shuffle_button = tk.Button(buttons_frame, text="Shuffle", command=self.shuffle)
        self.shuffle_button.pack(side=tk.LEFT, padx=5)

        self.deal_button = tk.Button(buttons_frame, text="Deal", command=self.deal, state=tk.DISABLED)
        self.deal_button.pack(side=tk.LEFT, padx=5)

        self.play_button = tk.Button(buttons_frame, text="Play", command=self.play, state=tk.DISABLED)
        self.play_button.pack(side=tk.LEFT, padx=5)

        # War resolution options (right side of bottom row)
        war_frame = tk.Frame(bottom_frame)
        war_frame.pack(side=tk.RIGHT, expand=True)

        tk.Label(war_frame, text="War Resolution:").pack()
        self.war_var = tk.StringVar(value="1")
        options = [("1 down", "1"), ("2 down", "2"), ("3 down", "3"), ("Speed", "speed")]
        for text, value in options:
            tk.Radiobutton(war_frame, text=text, variable=self.war_var, value=value).pack(anchor=tk.W)

    def shuffle(self):
        """Handle the Shuffle button click."""
        self.game.shuffle()
        self.deal_button.config(state=tk.NORMAL)
        self.shuffle_button.config(state=tk.DISABLED)
        messagebox.showinfo("Shuffled", "The deck has been shuffled.")

    def deal(self):
        """Handle the Deal button click."""
        self.game.deal()
        self.play_button.config(state=tk.NORMAL)
        self.deal_button.config(state=tk.DISABLED)
        self.update_player_labels()
        messagebox.showinfo("Dealt", "Cards have been dealt to the players.")

    def play(self):
        """Handle the Play button click."""
        winner = self.game.play_round()
        self.update_display()
        if winner:
            messagebox.showinfo("Game Over", f"{winner.name} wins the game!")
            self.root.quit()

    def update_display(self):
        """Update the GUI to reflect the current game state."""
        self.update_player_labels()
        self.update_card_display()

    def update_player_labels(self):
        """Update the labels showing the number of cards for each player."""
        self.player1_label.config(text=f"Player 1 - Remaining Cards: {len(self.game.players[0].hand)}")
        self.player2_label.config(text=f"Player 2 - Remaining Cards: {len(self.game.players[1].hand)}")

    def update_card_display(self):
        """Update the display of played cards."""
        card1 = self.game.table.played_cards.get(self.game.players[0].name)
        card2 = self.game.table.played_cards.get(self.game.players[1].name)

        self.player1_card.config(image=self.get_card_image(card1))
        self.player2_card.config(image=self.get_card_image(card2))

    def get_card_image(self, card) -> Optional[ImageTk.PhotoImage]:
        """Get the image for a given card."""
        if card is None:
            return None
        return self.card_images.get(f"{card.rank}{card.suit[0]}")

    def run(self):
        """Start the GUI main loop."""
        self.root.mainloop()