from .hand import Hand


class Dealer:
    def __init__(self):
        self.hand = Hand()

    def hit(self, card):
        self.hand.add_card(card)

    def get_value(self):
        return self.hand.calculate_value()

    def should_hit(self):
        return self.get_value() < 17