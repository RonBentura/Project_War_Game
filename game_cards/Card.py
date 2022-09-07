class Card:

    def __init__(self, symbol, value):
        self.symbol = symbol
        self.value = value

    def __gt__(self, other):
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
        if self.value == other.value and self.symbol == other.symbol:
            return True
        else:
            return False


    def cards_limit(self):
        if 1 > self.value or self.value > 13:
            raise TypeError('card have to be between 1-13 include')
        else:
            return True


