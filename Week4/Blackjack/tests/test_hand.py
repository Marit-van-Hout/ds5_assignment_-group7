from blackjack.hand import Hand


def test_number_cards():
    hand = Hand()

    hand.add_card("5C")
    hand.add_card("7H")

    assert hand.calculate_value() == 12


def test_face_cards_are_worth_10():
    hand = Hand()

    hand.add_card("KC")
    hand.add_card("QH")
    hand.add_card("JD")

    assert hand.calculate_value() == 30


def test_ace_counts_as_11_when_possible():
    hand = Hand()

    hand.add_card("AH")
    hand.add_card("7C")

    assert hand.calculate_value() == 18


def test_ace_changes_to_1_when_needed():
    hand = Hand()

    hand.add_card("AH")
    hand.add_card("KC")
    hand.add_card("5D")

    assert hand.calculate_value() == 16


def test_multiple_aces_are_handled():
    hand = Hand()

    hand.add_card("AH")
    hand.add_card("AD")
    hand.add_card("9C")

    assert hand.calculate_value() == 21