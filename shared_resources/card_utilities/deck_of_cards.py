""" Class to handle the generation, creation, and handling of the games' cards """


class StandardCardDeck(object):
    """ Handling the generation of a standard 52 card deck """

    def __init__(self, count, jokers=False):
        """
        Initialize class variables
        :param count: Number of decks to be included in the generation
        :param jokers: Boolean for jokers in deck
        """
        # Class public variables
        self.game_cards = self.__get_deck_for_game()

        # Class private variables
        self.__deck_count = count
        self.__jokers = jokers

    def __get_deck_for_game(self):
        """
        Get the total game deck based on the initialized variables
        :return:
        """
        deck = []
        if self.__jokers:
            cards = self.__generate_default_54_card_deck_2_jokers()
        else:
            cards = self.__generate_default_52_card_deck()
        for x in range(self.__deck_count):
            deck.append(cards)
        return deck

    def __generate_default_52_card_deck(self):
        """
        Generate default deck with no jokers
        :return:
        """
        return self.__fifty_two_card_deck()

    def __generate_default_54_card_deck_2_jokers(self):
        """
        Generate default 54 card deck with standard 2 jokers per deck
        :return:
        """
        return self.__fifty_two_card_deck(jokers=2)

    @staticmethod
    def __fifty_two_card_deck(jokers=0):
        """
        Generates a deck of cards with the expected number of jokers
        :param jokers:
        :return:
        """
        deck = []
        cards = ['A', 'K', 'Q', 'J']
        for num in range(2, 10):
            cards.append(str(num))
        for suit in ['Spades', 'Clubs', 'Diamonds', 'Hearts']:
            for card in cards:
                card_object = {
                    'suit': suit,
                    'card': card
                }
                deck.append(card_object)
        for x in range(jokers):
            card_object = {
                'suit': 'JOKER',
                'card': 'JOKER'
            }
            deck.append(card_object)
        return deck
