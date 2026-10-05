class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def calculate_value(self):
        total = 0
        aces = 0

        for card in self.cards:
            rank = card[:-1]

            if rank in ["J", "Q", "K"]:
                total += 10
            elif rank == "A":
                total += 11
                aces += 1
            else:
                total += int(rank)

        while total > 21 and aces > 0:
            total -= 10
            aces -= 1

        return total
    