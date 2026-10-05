from blackjack.deck import Deck


def test_deck_has_52_cards():
    deck = Deck()

    assert len(deck.cards) == 52


def test_deck_has_unique_cards():
    deck = Deck()

    assert len(set(deck.cards)) == 52


def test_draw_removes_card():
    deck = Deck()

    first_card_count = len(deck.cards)
    deck.draw_card()

    assert len(deck.cards) == first_card_count - 1