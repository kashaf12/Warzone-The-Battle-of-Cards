"""
Warzone: The Battle of Cards

This package contains the implementation of the card game
"Warzone: The Battle of Cards".

Modules:
    card: Defines the Card class
    deck: Implements the Deck class for managing a deck of cards
    player: Contains the Player class
    table: Implements the Table class for managing the game table
    rules: Defines the Rules class for game variations
    game: Implements the main Game logic
    gui: Contains the GUI class for the graphical user interface
"""

from .card import Card
from .deck import Deck
from .player import Player
from .table import Table
from .rules import Rules
from .game import Game
from .gui import GUI

__all__ = ['Card', 'Deck', 'Player', 'Table', 'Rules', 'Game', 'GUI']

__version__ = "1.0.0"
__author__ = "Kashaf Ahmed"
__email__ = "kashafaahmed@gmail.com"