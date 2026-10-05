from .deck import Deck
from .player import Player
from .dealer import Dealer


class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()

    def setup_round(self):
        self.deck = Deck()
        self.deck.shuffle()

        self.player = Player()
        self.dealer = Dealer()

        self.player.hit(self.deck.draw_card())
        self.player.hit(self.deck.draw_card())

        self.dealer.hit(self.deck.draw_card())
        self.dealer.hit(self.deck.draw_card())

    def player_turn(self):
        while True:
            print(f"Player cards: {self.player.hand.cards}")
            print(f"Player total: {self.player.get_value()}")
            print(f"Dealer up card: {self.dealer.hand.cards[0]}")

            action = self.player.choose_action()

            if action == "H":
                self.player.hit(self.deck.draw_card())

                if self.player.get_value() > 21:
                    return "player_bust"

            else:
                return "stand"

    def dealer_turn(self):
        while self.dealer.should_hit():
            self.dealer.hit(self.deck.draw_card())

    def determine_winner(self):
        player_total = self.player.get_value()
        dealer_total = self.dealer.get_value()

        if player_total > 21:
            return "Dealer won"

        if dealer_total > 21:
            return "You won"

        if player_total > dealer_total:
            return "You won"

        return "Dealer won"

    def play_round(self):
        self.setup_round()

        player_result = self.player_turn()

        if player_result == "player_bust":
            return self.finish_game("Dealer won")

        self.dealer_turn()

        return self.finish_game(self.determine_winner())

    def finish_game(self, result):
        print("\n--- Final Result ---")
        print(f"Player cards: {self.player.hand.cards}")
        print(f"Player total: {self.player.get_value()}")
        print(f"Dealer cards: {self.dealer.hand.cards}")
        print(f"Dealer total: {self.dealer.get_value()}")
        print(result)

        return result
    