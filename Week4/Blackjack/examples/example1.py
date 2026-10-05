from blackjack.hand import Hand


def main():
    hand = Hand()

    hand.add_card("AH")
    hand.add_card("7C")

    print("Example 1: Blackjack Hand")
    print("Cards:", hand.cards)
    print("Total:", hand.calculate_value())


if __name__ == "__main__":
    main()