""" Unit tests for the deck of cards resource """
from shared_resources.card_utilities.deck_of_cards import StandardCardDeck, EuchreCardDeck

from unittest import TestCase


class TestStandardCardDeck(TestCase):
    """ Unit tests for the StandardCardDeck class """

    def test_standard_52_card_deck(self):
        """ Test to verify that a standard 52 card deck can be generated
        1. Generate the test variables
        2. Verify the card count
        3. Verify the contents of the cards
        """
        # 1. Generate the test variables
        deck_class = StandardCardDeck()
        deck = deck_class.game_cards
        test_card = {'suit': 'Spades', 'card': '9'}

        # 2. Verify the card count
        self.assertEqual(52, len(deck))

        # 3. Verify the contents of the cards
        self.assertIn(test_card, deck)

    def test_standard_54_card_deck_with_jokers(self):
        """ Test to verify a standard 54 card deck with jokers can be generated
        1. Generate the test variables
        2. Verify the card count
        3. Verify the contents of the cards
        """
        # 1. Generate the test variables
        deck_class = StandardCardDeck(1, True)
        deck = deck_class.game_cards
        test_card = {'suit': 'Spades', 'card': '9'}
        test_joker = {'suit': 'JOKER', 'card': 'JOKER'}

        # 2. Verify the card count
        self.assertEqual(54, len(deck))

        # 3. Verify the contents of the cards
        self.assertIn(test_card, deck)
        self.assertIn(test_joker, deck)

    def test_double_deck_with_jokers(self):
        """ Test to verify a double deck with jokers can be generated
        1. Generate the test variables
        2. Verify the card count
        3. Verify the contents of the cards
        """
        # 1. Generate the test variables
        deck_class = StandardCardDeck(2, True)
        deck = deck_class.game_cards
        test_card = {'suit': 'Spades', 'card': '9'}
        test_joker = {'suit': 'JOKER', 'card': 'JOKER'}

        # 2. Verify the card count
        self.assertEqual(108, len(deck))

        # 3. Verify the contents of the cards
        self.assertIn(test_card, deck)
        self.assertIn(test_joker, deck)

    def test_double_deck(self):
        """ Test to verify a double deck without jokers can be generated
        1. Generate the test variables
        2. Verify the card count
        3. Verify the contents of the cards
        """
        # 1. Generate the test variables
        deck_class = StandardCardDeck(2, False)
        deck = deck_class.game_cards
        test_card = {'suit': 'Spades', 'card': '9'}

        # 2. Verify the card count
        self.assertEqual(104, len(deck))

        # 3. Verify the contents of the cards
        self.assertIn(test_card, deck)

    def test_euchre_deck(self):
        """ Test to verify a euchre deck can be generated
        1. Generate the test variables
        2. Verify the card count
        3. Verify the contents of the cards
        """
        # 1. Generate the test variables
        deck_class = EuchreCardDeck()
        deck = deck_class.game_cards
        test_card = {'suit': 'Spades', 'card': '9'}

        # 2. Verify the card count
        self.assertEqual(32, len(deck))

        # 3. Verify the contents of the cards
        self.assertIn(test_card, deck)
