import unittest

from playing_card import PlayingCard

class TestPlayingCard(unittest.TestCase):

    def test_valid_card(self):
        card = PlayingCard("A", "Hearts")
        self.assertEqual(str(card), "A of Hearts")

    def test_invalid_rank(self):
        with self.assertRaises(ValueError):
            PlayingCard("1", "Hearts")

    def test_invalid_suit(self):
        with self.assertRaises(ValueError):
            PlayingCard("A", "Stars")

    def test_card_equality(self):
        card1 = PlayingCard("10", "Diamonds")
        card2 = PlayingCard("10", "Diamonds")
        self.assertEqual(card1, card2)

    def test_card_inequality(self):
        card1 = PlayingCard("10", "Diamonds")
        card2 = PlayingCard("J", "Diamonds")
        self.assertNotEqual(card1, card2)

import unittest

class TestHand(unittest.TestCase):

    def setUp(self):
        """This method runs before every test."""
        self.hand = Hand()

    def test_add_card(self):
        """Test adding a card to the hand."""
        self.hand.add_card("Ace of Spades")
        self.assertEqual(self.hand.num_cards(), 1)
        self.assertIn("Ace of Spades", self.hand.cards)
    
    def test_display_hand(self):
        """Test displaying the hand of cards."""
        self.hand.add_card("Ace of Spades")
        self.hand.add_card("10 of Hearts")
        self.assertEqual(self.hand.display_hand(), "Ace of Spades, 10 of Hearts")

        # Test empty hand case
        empty_hand = Hand()
        self.assertEqual(empty_hand.display_hand(), "No cards in hand.")
    
    def test_num_cards(self):
        """Test the number of cards in the hand."""
        self.assertEqual(self.hand.num_cards(), 0)
        self.hand.add_card("Ace of Spades")
        self.assertEqual(self.hand.num_cards(), 1)
        self.hand.add_card("10 of Hearts")
        self.assertEqual(self.hand.num_cards(), 2)
        self.hand.add_card("Queen of Diamonds")
        self.assertEqual(self.hand.num_cards(), 3)
    
    def test_empty_hand(self):
        """Test behavior with an empty hand."""
        empty_hand = Hand()
        self.assertEqual(empty_hand.num_cards(), 0)
        self.assertEqual(empty_hand.display_hand(), "No cards in hand.")
    
    def test_multiple_cards(self):
        """Test adding multiple cards and the result."""
        cards = ["Ace of Spades", "2 of Hearts", "King of Diamonds"]
        for card in cards:
            self.hand.add_card(card)
        self.assertEqual(self.hand.num_cards(), len(cards))
        self.assertEqual(self.hand.display_hand(), ', '.join(cards))


if __name__ == '__main__':
    unittest.main()

    

class TestHand(unittest.TestCase):

    def setUp(self):
        """This method runs before every test."""
        self.hand = Hand()

    def test_add_card(self):
        """Test adding a card to the hand."""
        self.hand.add_card("Ace of Spades")
        self.assertEqual(self.hand.num_cards(), 1)
        self.assertIn("Ace of Spades", self.hand.cards)
    
    def test_display_hand(self):
        """Test displaying the hand of cards."""
        self.hand.add_card("Ace of Spades")
        self.hand.add_card("10 of Hearts")
        self.assertEqual(self.hand.display_hand(), "Ace of Spades, 10 of Hearts")

        # Test empty hand case
        empty_hand = Hand()
        self.assertEqual(empty_hand.display_hand(), "No cards in hand.")
    
    def test_num_cards(self):
        """Test the number of cards in the hand."""
        self.assertEqual(self.hand.num_cards(), 0)
        self.hand.add_card("Ace of Spades")
        self.assertEqual(self.hand.num_cards(), 1)
        self.hand.add_card("10 of Hearts")
        self.assertEqual(self.hand.num_cards(), 2)
        self.hand.add_card("Queen of Diamonds")
        self.assertEqual(self.hand.num_cards(), 3)
    
    def test_empty_hand(self):
        """Test behavior with an empty hand."""
        empty_hand = Hand()
        self.assertEqual(empty_hand.num_cards(), 0)
        self.assertEqual(empty_hand.display_hand(), "No cards in hand.")
    
    def test_multiple_cards(self):
        """Test adding multiple cards and the result."""
        cards = ["Ace of Spades", "2 of Hearts", "King of Diamonds"]
        for card in cards:
            self.hand.add_card(card)
        self.assertEqual(self.hand.num_cards(), len(cards))
        self.assertEqual(self.hand.display_hand(), ', '.join(cards))


if __name__ == '__main__':
    unittest.main()
