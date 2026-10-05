from blackjack.player import Player


def test_player_starts_with_empty_hand():
    player = Player()

    assert player.hand.cards == []


def test_player_can_receive_card():
    player = Player()

    player.hit("AH")

    assert player.hand.cards == ["AH"]


def test_player_value_is_calculated():
    player = Player()

    player.hit("KC")
    player.hit("7H")

    assert player.get_value() == 17