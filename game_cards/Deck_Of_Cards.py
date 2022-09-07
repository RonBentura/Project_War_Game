from Card import Card
from random import randint
from random import shuffle

class DeckOfCards:

    def __init__(self):
        self.d1 = {'diamond': 1, 'spade': 2, 'heart': 3, 'club': 4}
        self.list1 = []
        for shape in self.d1.keys():
            for i in range(1, 14):
                new_card = Card(shape, i)
                self.list1.append(new_card)

    def cards_shuffle(self):
        shuffle(self.list1)

    def deal_one(self):
        x = randint(0, len(self.list1))
        self.list1.pop(x)










    def cadrs_shuffle(self):
        shuffle()
