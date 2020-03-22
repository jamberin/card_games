""" Class to handle the generation, creation, and handling of the games' cards """


class StandardCardDeck(object):
    """ Handling the generation of a standard 52 card deck """

    def __init__(self, count=1, jokers=False):
        """
        Initialize Class
        :param count: Number of decks to be included in the generation
        :param jokers: Boolean for jokers in deck
        """
        self.game_cards = self.__get_deck_for_game(count, jokers)

    def __get_deck_for_game(self, count, jokers):
        """
        Get the total game deck based on the initialized variables
        :return:
        """
        deck = []
        if jokers:
            cards = self.__generate_default_54_card_deck_2_jokers()
        else:
            cards = self.__generate_default_52_card_deck()
        for x in range(count):
            deck.extend(cards)
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
        for num in range(2, 11):
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


class EuchreCardDeck(object):
    """ Game deck for euchre game """

    def __init__(self, count=1):
        """
        Initialize Class
        :param count:
        """
        self.game_cards = self.__get_deck_for_game(count)

    @staticmethod
    def __get_default_deck():
        """ Generates a default deck of cards for a game of euchre """
        deck = []
        cards = ['A', 'K', 'Q', 'J']
        for num in range(7, 11):
            cards.append(str(num))
        for suit in ['Spades', 'Clubs', 'Diamonds', 'Hearts']:
            for card in cards:
                card_object = {
                    'suit': suit,
                    'card': card
                }
                deck.append(card_object)
        return deck

    def __get_deck_for_game(self, count):
        """
        Get the total game deck based on the initialized variables
        :return:
        """
        deck = []
        cards = self.__get_default_deck()
        for x in range(count):
            deck.extend(cards)
        return deck
