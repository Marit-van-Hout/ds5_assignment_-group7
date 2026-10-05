def show_player_decision_state(player, dealer):
    print(f"Player cards: {player.hand.cards}")
    print(f"Player total: {player.get_value()}")
    print(f"Dealer up card: {dealer.hand.cards[0]}")


def show_final_result(player, dealer, result):
    print("\n--- Final Result ---")
    print(f"Player cards: {player.hand.cards}")
    print(f"Player total: {player.get_value()}")
    print(f"Dealer cards: {dealer.hand.cards}")
    print(f"Dealer total: {dealer.get_value()}")
    print(result)