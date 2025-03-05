class PlayingCard:
    """A playing card class"""
    
    SUITS = ("Hearts", "Diamonds", "Clubs", "Spades")
    RANKS = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")

    def __init__(self, rank, suit):
        if rank not in self.RANKS:
            raise ValueError("Invalid rank")
        if suit not in self.SUITS:
            raise ValueError("Invalid suit")
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __eq__(self, other):
        if not isinstance(other, PlayingCard):
            return False
        return self.rank == other.rank and self.suit == other.suit
class Deck:
    def __init__self():
            self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
            self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
            self.deck = self.generate_deck()
            
    def generate_deck(self):
        """Generates a deck of 52 cards."""
        return [f'{rank} of {suit}' for suit in self.suits for rank in self.ranks]

    def shuffle(self):
        """Shuffles the deck."""
        random.shuffle(self.deck)
        
    def draw_card(self):
        """Draws a card from the deck."""
        if len(self.deck) > 0:
            return self.deck.pop()
        else:
            return "No more cards in the deck."
        
        def __str__(self):
            return ', '.join(self.deck)
        
class Hand:
    def __init__(self):
        self.cards = []  # This will hold the cards in the hand
    
    def add_card(self, card):
        """Adds a card to the hand."""
        self.cards.append(card)
    
    def display_hand(self):
        """Displays the hand of cards."""
        if self.cards:
            return ', '.join(self.cards)
        else:
            return "No cards in hand."
    
    def num_cards(self):
        """Returns the number of cards in the hand."""
        return len(self.cards)

        