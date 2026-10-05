from .hand import Hand


class Player:
    def __init__(self):
        self.hand = Hand()

    def hit(self, card):
        self.hand.add_card(card)

    def get_value(self):
        return self.hand.calculate_value()

    def choose_action(self):
        while True:
            action = input("Hit or Stand? (H/S): ").strip().upper()

            if action in ["H", "S"]:
                return action

            print("Invalid input. Please enter H or S.")