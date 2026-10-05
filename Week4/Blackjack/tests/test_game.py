from blackjack.game import BlackjackGame


def test_new_game_has_empty_hands():
    game = BlackjackGame()

    assert game.player.hand.cards == []
    assert game.dealer.hand.cards == []


def test_setup_round_deals_two_cards_each():
    game = BlackjackGame()

    game.setup_round()

    assert len(game.player.hand.cards) == 2
    assert len(game.dealer.hand.cards) == 2


def test_setup_round_has_48_cards_left():
    game = BlackjackGame()

    game.setup_round()

    assert len(game.deck.cards) == 48


def test_dealer_stops_at_17_or_more():
    game = BlackjackGame()

    game.setup_round()

    game.dealer_turn()

    assert game.dealer.get_value() >= 17


def test_player_bust_means_dealer_wins():
    game = BlackjackGame()

    game.player.hand.cards = ["KC", "QD", "5H"]

    result = game.determine_winner()

    assert result == "Dealer won"