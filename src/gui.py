
import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from typing import Dict, Optional
from .game import Game
from .rules import Rules
from .card import Card

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
        window = tk.Toplevel # needed to fix tkinter image rendering bug https://stackoverflow.com/questions/23224574/tkinter-create-image-function-error-pyimage1-does-not-exist
        self.game = game
        self.root = tk.Tk()
        self.root.title("Warzone: The Battle of Cards")
        self.root.geometry("800x600")

        self.card_images = self.load_card_images()

        self.war_var = tk.StringVar(value="1")
        self.war_var.trace_add("write", self.update_rules)
        
        self.create_widgets()
        self.shuffle() 

    def load_card_images(self) -> Dict[str, ImageTk.PhotoImage]:
        """
        Load card images from files.

        Returns:
            Dict[str, ImageTk.PhotoImage]: A dictionary of card images.
        """
        images = {}
        card_size = (150, 218)  # Adjust this size as needed
        
        # Load the back of the card
        back_path = os.path.join("static", "images", "DECK", "gray_back.png")
        if os.path.exists(back_path):
            back_image = Image.open(back_path).resize(card_size, Image.LANCZOS)
            images['back'] = ImageTk.PhotoImage(back_image)
        else:
            print(f"Warning: Back card image not found at {back_path}")

        back_deck_path = os.path.join("static", "images", "DECK", "back_cards-07.png")
        if os.path.exists(back_deck_path):
            back_deck_image = Image.open(back_deck_path).resize((350,350), Image.LANCZOS)
            images['back_deck'] = ImageTk.PhotoImage(back_deck_image)
        else:
            print(f"Warning: Back deck image not found at {back_deck_path}")

        # Load all other card images
        ranks = ['A'] + [str(i) for i in range(2, 11)] + ['J', 'Q', 'K']
        suits = ['H', 'D', 'C', 'S']

        for rank in ranks:
            for suit in suits:
                filename = f"{rank}{suit}.png"
                filepath = os.path.join("static", "images", "DECK", filename)
                if os.path.exists(filepath):
                    card_image = Image.open(filepath).resize(card_size, Image.LANCZOS)
                    images[f"{rank}{suit}"] = ImageTk.PhotoImage(card_image)
                else:
                    print(f"Warning: Image file not found for {filename}")

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

        # Middle frame for winner display
        self.middle_frame = tk.Frame(top_frame, width=200)
        self.middle_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.winner_label = tk.Label(self.middle_frame, text="", font=("Arial", 16, "bold"))
        self.winner_label.pack(expand=True)

        # Bottom row (smaller)
        bottom_frame = tk.Frame(self.root)
        bottom_frame.pack(fill=tk.X)

        # Buttons frame (left side of bottom row)
        buttons_frame = tk.Frame(bottom_frame)
        buttons_frame.pack(side=tk.LEFT, expand=True)

        # Add a new label for the deck in the center
        self.deck_label = tk.Label(top_frame)
        self.deck_label.pack(expand=True)

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

    def update_rules(self, *args):
        """Update game rules when war resolution method changes."""
        self.game.rules.war_resolution_method = self.war_var.get()
        self.update_display()  # Refresh the display to reflect any changes
        
        # Update status message
        if self.game.is_war_in_progress():
            self.update_war_status()
        else:
            self.winner_label.config(text=f"War resolution method changed to: {self.war_var.get()}")

    def update_war_status(self):
        """Update the status message during a war."""
        if self.game.rules.war_resolution_method == 'speed':
            self.winner_label.config(text="Speed War! Click 'Resolve War' to continue.")
        else:
            self.winner_label.config(text=f"War! {self.game.rules.war_resolution_method} down. Click 'Resolve War' to continue.")


    def shuffle(self):
        """Handle the Shuffle button click."""
        self.game = Game(self.game.players[0].name, self.game.players[1].name, self.game.rules)
        self.game.shuffle()
        self.deal_button.config(state=tk.NORMAL)
        self.play_button.config(state=tk.DISABLED)
        self.update_display()
        self.winner_label.config(text="")
        self.root.title("Warzone: The Battle of Cards - The deck has been shuffled.")

    def deal(self):
        """Handle the Deal button click."""
        self.game.deal()
        self.play_button.config(state=tk.NORMAL)
        self.deal_button.config(state=tk.DISABLED)
        self.update_display()
        self.root.title("Warzone: The Battle of Cards - Cards have been dealt to the players.")

    def play(self):
        if self.game.is_war_in_progress():
            winner = self.game.resolve_war()
        else:
            winner = self.game.play_round()
        self.update_display()
        if winner:
            self.winner_label.config(text=f"{winner.name} wins the game!")
            messagebox.showinfo("Game Over", f"{winner.name} wins the game!")
            self.shuffle()  # Reset the game
        elif self.game.is_war_in_progress():
            self.update_war_status()
            self.play_button.config(text="Resolve War")
        else:
            round_winner = self.game.table.get_round_winner()
            if round_winner:
                self.winner_label.config(text=f"{round_winner} wins the round!")
            else:
                self.winner_label.config(text="It's a tie!") 
            self.play_button.config(text="Play")   

    def update_display(self):
        """Update the GUI to reflect the current game state."""
        self.update_player_labels()
        self.update_card_display()
        self.update_deck_display()
        

    def update_player_labels(self):
        """Update the labels showing the number of cards for each player and whose turn it is."""
        for i, player in enumerate(self.game.players, 1):
            label = getattr(self, f'player{i}_label')
            if player.hand:
                label.config(text=f"Player {i} - Remaining Cards: {len(player.hand)}")
            else:
                label.config(text=f"Player {i} - No Cards")  

    def update_card_display(self):
        for i, player in enumerate(self.game.players, 1):
            card_label = getattr(self, f'player{i}_card')
            if player.hand:
                if self.game.table.played_cards.get(player.name):
                    card = self.game.table.played_cards[player.name]
                elif self.game.table.last_played_cards.get(player.name):
                    card = self.game.table.last_played_cards[player.name]
                else:
                    card = None
                
                if card:
                    card_image = self.get_card_image(card)
                    if card_image:
                        card_label.config(image=card_image)
                        card_label.image = card_image
                    else:
                        print(f"Failed to load image for card: {card}")
                        card_label.config(image='')
                else:
                    back_image = self.card_images.get('back')
                    if back_image:
                        card_label.config(image=back_image)
                        card_label.image = back_image
                    else:
                        print("Failed to load back image")
                        card_label.config(image='')
            else:
                card_label.config(image='')
                
    def update_deck_display(self):
        """Update the display of deck."""
        try:
            if not self.game.players[0].hand and not self.game.players[1].hand:
                self.deck_label.config(image=self.card_images['back_deck'])
            else:
                self.deck_label.config(image='')
        except:
            print("failed to load update_deck_display")        
    
    def get_card_image(self, card: Optional[Card]) -> Optional[ImageTk.PhotoImage]:
        """
        Get the image for a given card.

        Args:
            card (Optional[Card]): The card object to get the image for.

        Returns:
            Optional[ImageTk.PhotoImage]: The image of the card, or None if the card is None.
        """
        if card is None:
            return None
        
        if card.facedown:
            return self.card_images['back']
        
        rank = card.rank
        suit = card.suit[0].upper()
        return self.card_images.get(f"{rank}{suit}")

    def run(self):
        """Start the GUI main loop."""
        self.root.mainloop()