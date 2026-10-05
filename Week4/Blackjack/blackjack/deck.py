import random


class Deck:
    def __init__(self):
        self.ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10",
                      "J", "Q", "K", "A"]
        self.suits = ["C", "D", "H", "S"]

        self.cards = []
        for suit in self.suits:
            for rank in self.ranks:
                self.cards.append(rank + suit)

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        if len(self.cards) == 0:
            raise ValueError("The deck is empty.")

        return self.cards.pop()