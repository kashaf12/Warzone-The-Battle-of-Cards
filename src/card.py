import os
from PIL import Image, ImageTk

class Card:
    """
    Represents a playing card in the Warzone game.

    This class defines a card with a rank and suit, provides methods
    for comparing cards based on their rank, and a method to get the card's image.

    Attributes:
        rank (str): The rank of the card (e.g., '2', '3', ..., 'J', 'Q', 'K', 'A').
        suit (str): The suit of the card (Hearts, Diamonds, Clubs, Spades).
        facedown (bool): Indicates whether the card is face down (default is False).

    Class Attributes:
        RANKS (list): Valid card ranks in ascending order.
        SUITS (list): Valid card suits.
        IMAGE_PATH (str): Path to the directory containing card images.
    """

    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    IMAGE_PATH = os.path.join("static", "images", "DECK")

    def __init__(self, rank: str, suit: str):
        """
        Initialize a new Card instance.

        Args:
            rank (str): The rank of the card.
            suit (str): The suit of the card.

        Raises:
            ValueError: If an invalid rank or suit is provided.
        """
        if rank not in self.RANKS:
            raise ValueError(f"Invalid rank: {rank}")
        if suit not in self.SUITS:
            raise ValueError(f"Invalid suit: {suit}")
        
        self.rank = rank
        self.suit = suit
        self.facedown = False

    def __str__(self) -> str:
        """
        Return a string representation of the card.

        Returns:
            str: A string in the format "rank of suit" (e.g., "Ace of Spades").
        """
        return f"{self.rank} of {self.suit}"

    def get_value(self) -> int:
        """
        Get the numeric value of the card based on its rank.

        Returns:
            int: The value of the card (2-14, where Ace is 14).
        """
        return self.RANKS.index(self.rank) + 2

    def __lt__(self, other: 'Card') -> bool:
        """
        Compare this card with another card for "less than" relationship.

        Args:
            other (Card): The other card to compare with.

        Returns:
            bool: True if this card's value is less than the other card's value, False otherwise.
        """
        return self.get_value() < other.get_value()

    def __gt__(self, other: 'Card') -> bool:
        """
        Compare this card with another card for "greater than" relationship.

        Args:
            other (Card): The other card to compare with.

        Returns:
            bool: True if this card's value is greater than the other card's value, False otherwise.
        """
        return self.get_value() > other.get_value()

    def __eq__(self, other: 'Card') -> bool:
        """
        Compare this card with another card for equality.

        Args:
            other (Card): The other card to compare with.

        Returns:
            bool: True if this card's value is equal to the other card's value, False otherwise.
        """
        return self.get_value() == other.get_value()

    def compare(self, other_card: 'Card') -> int:
        """
        Compare the rank of this card with another card.

        Args:
            other_card (Card): The other card to compare with.

        Returns:
            int: 1 if this card's rank is higher, -1 if lower, and 0 if equal.
        """
        if self > other_card:
            return 1
        elif self < other_card:
            return -1
        else:
            return 0

    def get_image(self, size: tuple = (100, 145)) -> ImageTk.PhotoImage:
        """
        Get the image of the card (front face).

        Args:
            size (tuple): The desired size of the image (width, height).

        Returns:
            ImageTk.PhotoImage: The image of the card resized to the specified dimensions.

        Raises:
            FileNotFoundError: If the image file for the card is not found.
        """
        suit_letter = self.suit[0].upper()
        filename = f"{self.rank}{suit_letter}.png"
        filepath = os.path.join(self.IMAGE_PATH, filename)
        
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Card image not found: {filepath}")
        
        image = Image.open(filepath)
        image = image.resize(size, Image.LANCZOS)
        return ImageTk.PhotoImage(image)