class Card:

    def __init__(self, symbol, value):
        self.symbol = symbol
        self.value = value

    def __gt__(self, other):
        """method that compering the values of cards to find out who is bigger"""
        if self.value == other.value:
            return self.symbol > other.symbol
        if self.value == 1:
            return True
        if other.value == 1:
            return False
        if self.value > other.value:
            return True
        else:
            return False

    # unit test
    def __eq__(self, other):
        """method that created for tests if we poped out a card and the card didnt stayed in the deck"""
        if self.value == other.value and self.symbol == other.symbol:
            return True
        else:
            return False


    def cards_limit(self):
        """method that put the int limits for the card values"""
        if 1 > self.value or self.value > 13:
            raise TypeError('card have to be between 1-13 include')
        else:
            return True

    def __repr__(self):
        return f"{self.value}{self.symbol}"
