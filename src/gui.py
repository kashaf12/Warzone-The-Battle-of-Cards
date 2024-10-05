# src/gui.py

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

class GUI:
    def __init__(self, game):
        self.game = game
        self.root = tk.Tk()
        self.root.title("Warzone: The Battle of Cards")
        
        # Set window size
        self.root.geometry("1000x600")

        # Create a frame with green background
        self.table_frame = tk.Frame(self.root, bg="#2F4F4F", width=1000, height=600)
        self.table_frame.pack_propagate(0)
        self.table_frame.pack(fill=tk.BOTH, expand=True)

        self.card_images = self.load_card_images()

        # Game status label at the top
        self.status_label = tk.Label(self.table_frame, text="Welcome to Warzone!", bg="#2F4F4F", fg="white", font=("Arial", 16))
        self.status_label.pack(pady=20)

        # Create a frame for players
        self.players_frame = tk.Frame(self.table_frame, bg="#2F4F4F")
        self.players_frame.pack(expand=True, fill=tk.BOTH)

        # Player 1 area (left)
        self.player1_frame = tk.Frame(self.players_frame, bg="#2F4F4F", width=400)
        self.player1_frame.pack(side=tk.LEFT, padx=20, expand=True, fill=tk.BOTH)
        
        self.player1_label = tk.Label(self.player1_frame, text=str(self.game.players[0]), 
                                      bg="#2F4F4F", fg="white", font=("Arial", 14))
        self.player1_label.pack(pady=10)

        self.player1_card = tk.Label(self.player1_frame, bg="#2F4F4F")
        self.player1_card.pack(pady=10)

        # Player 2 area (right)
        self.player2_frame = tk.Frame(self.players_frame, bg="#2F4F4F", width=400)
        self.player2_frame.pack(side=tk.RIGHT, padx=20, expand=True, fill=tk.BOTH)

        self.player2_label = tk.Label(self.player2_frame, text=str(self.game.players[1]), 
                                      bg="#2F4F4F", fg="white", font=("Arial", 14))
        self.player2_label.pack(pady=10)

        self.player2_card = tk.Label(self.player2_frame, bg="#2F4F4F")
        self.player2_card.pack(pady=10)

        # Buttons frame at the bottom
        self.buttons_frame = tk.Frame(self.table_frame, bg="#2F4F4F")
        self.buttons_frame.pack(side=tk.BOTTOM, pady=20)

        self.shuffle_button = tk.Button(self.buttons_frame, text="Shuffle", command=self.shuffle,
                                        font=("Arial", 14), bg="#DAA520", fg="black")
        self.shuffle_button.pack(side=tk.LEFT, padx=10)

        self.deal_button = tk.Button(self.buttons_frame, text="Deal", command=self.deal,
                                     font=("Arial", 14), bg="#DAA520", fg="black", state=tk.DISABLED)
        self.deal_button.pack(side=tk.LEFT, padx=10)

        self.play_button = tk.Button(self.buttons_frame, text="Play", command=self.play,
                                     font=("Arial", 14), bg="#DAA520", fg="black", state=tk.DISABLED)
        self.play_button.pack(side=tk.LEFT, padx=10)

        self.update_display()

    def load_card_images(self):
        images = {}
        deck_folder = os.path.join("static", "images", "DECK")
        
        print(f"Loading images from: {deck_folder}")
        
        # Load face-up card images
        for suit in ['H', 'D', 'C', 'S']:
            for rank in ['A'] + [str(n) for n in range(2, 11)] + ['J', 'Q', 'K']:
                filename = f"{rank}{suit}.png"
                filepath = os.path.join(deck_folder, filename)
                if os.path.exists(filepath):
                    image = Image.open(filepath)
                    image = image.resize((100, 145), Image.LANCZOS)
                    images[filename] = ImageTk.PhotoImage(image)
                    print(f"Loaded: {filename}")
                else:
                    print(f"Warning: {filename} not found")

        # Load card back image
        back_filepath = os.path.join(deck_folder, "back_cards-07.png")
        if os.path.exists(back_filepath):
            back_image = Image.open(back_filepath)
            back_image = back_image.resize((100, 145), Image.LANCZOS)
            images["back"] = ImageTk.PhotoImage(back_image)
            print("Loaded: back_cards-07.png")
        else:
            print("Warning: back_cards-07.png not found")

        print(f"Total images loaded: {len(images)}")
        return images
    def get_card_image(self, card):
        if card is None:
            print("Attempting to get image for None card")
            return self.card_images.get("back")
        if card.facedown:
            print(f"Getting back image for face-down card: {card}")
            return self.card_images.get("back")
        else:
            filename = f"{card.rank}{card.suit[0]}.png"
            print(f"Getting image for card: {card}, filename: {filename}")
            image = self.card_images.get(filename)
            if image is None:
                print(f"Warning: Image not found for {filename}")
                return self.card_images.get("back")
            return image

    def shuffle(self):
        self.game.shuffle()
        self.status_label.config(text="Deck shuffled. Ready to deal.")
        self.deal_button.config(state=tk.NORMAL)
        self.shuffle_button.config(state=tk.DISABLED)

    def deal(self):
        self.game.deal()
        self.status_label.config(text="Cards dealt. Ready to play.")
        self.play_button.config(state=tk.NORMAL)
        self.deal_button.config(state=tk.DISABLED)
        self.update_display()

    def play_round(self):
        print("\n--- Playing a round ---")
        winner = self.game.play_round()
        if winner:
            messagebox.showinfo("Game Over", f"{winner.name} wins the game!")
            self.root.quit()
        else:
            self.update_display()

    def play(self):
        winner = self.game.play_round()
        if winner:
            messagebox.showinfo("Game Over", f"{winner.name} wins the game!")
            self.root.quit()
        else:
            self.update_display()        

    def update_display(self):
        self.player1_label.config(text=f"{self.game.players[0].name} ({len(self.game.players[0].hand)} cards)")
        self.player2_label.config(text=f"{self.game.players[1].name} ({len(self.game.players[1].hand)} cards)")

        card1 = self.game.table.played_cards.get(self.game.players[0].name)
        card2 = self.game.table.played_cards.get(self.game.players[1].name)

        print(f"Player 1 card: {card1}")
        print(f"Player 2 card: {card2}")

        image1 = self.get_card_image(card1) if card1 else self.card_images.get("back")
        image2 = self.get_card_image(card2) if card2 else self.card_images.get("back")

        print(f"Image 1: {image1}")
        print(f"Image 2: {image2}")

        self.player1_card.config(image=image1)
        self.player1_card.image = image1  # Keep a reference to prevent garbage collection
        self.player2_card.config(image=image2)
        self.player2_card.image = image2  # Keep a reference to prevent garbage collection

        if self.game.table.played_cards:
            self.status_label.config(text=f"Cards played. {self.game.get_round_winner().name} wins the round.")
        elif len(self.game.players[0].hand) == 26:
            self.status_label.config(text="Cards dealt. Ready to play.")
        else:
            self.status_label.config(text="Ready for next round.")
    def run(self):
        self.root.mainloop()