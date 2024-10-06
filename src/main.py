
from src.game import Game
from src.rules import Rules
from src.gui import GUI

def main():
    """
    Main function to set up and run the Warzone: The Battle of Cards game.
    """
    
    # Get player names
    player1_name = "Player 1"
    player2_name = "Player 2"

    # Set up the game rules
    rules = Rules(
        war_resolution_method='1',
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