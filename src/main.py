
from .game import Game
from .gui import GUI

def main():
    game = Game("Player 1", "Player 2")
    gui = GUI(game)
    gui.run()

if __name__ == "__main__":
    main()