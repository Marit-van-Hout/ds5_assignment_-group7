from blackjack.deck import Deck


def main():
    deck = Deck()
    deck.shuffle()

    print("Example 2: Drawing Cards")
    print("First card:", deck.draw_card())
    print("Second card:", deck.draw_card())
    print("Cards remaining:", len(deck.cards))


if __name__ == "__main__":
    main()