import tkinter as tk
from tkinter import simpledialog
from src.game import Game
from src.rules import Rules
from src.gui import GUI

def get_player_name(player_number):
    """
    Prompt the user to enter a player name.

    Args:
        player_number (int): The number of the player (1 or 2).

    Returns:
        str: The name entered by the user, or a default name if none is provided.
    """
    name = simpledialog.askstring("Player Name", f"Enter name for Player {player_number}:")
    return name if name else f"Player {player_number}"

def main():
    """
    Main function to set up and run the Warzone: The Battle of Cards game.
    """
    # Create the root window
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Get player names
    player1_name = get_player_name(1)
    player2_name = get_player_name(2)

    # Set up the game rules
    rules = Rules(
        war_resolution_method='standard',
        use_double_deck=False,
        speed_war_enabled=False
    )

    # Create the game instance
    game = Game(player1_name, player2_name, rules)

    # Create and run the GUI
    gui = GUI(game)
    gui.run()

if __name__ == "__main__":
    main()