# Blackjack Project Plan

## 1. Project Goal

Create a simple text-based Blackjack game in Python using one standard 52-card deck.

The game should allow a player to play against a dealer according to the rules specified in the assignment.

## 2. Card and Deck Management

This component is responsible for creating and managing the deck.

It should:

- Create a standard 52-card deck.
- Use the ranks 2–10, J, Q, K and A.
- Use the suits C, D, H and S.
- Shuffle the deck at the start of each round.
- Draw cards without replacement.

## 3. Card Values and Hand Calculation

This component is responsible for calculating the value of a hand.

The rules are:

- Cards 2–10 are worth their numerical value.
- J, Q and K are worth 10.
- An Ace initially counts as 11.
- If the total exceeds 21 and the hand contains an Ace counted as 11, that Ace is changed to 1.
- This process should be repeated when necessary for hands containing multiple Aces.

The component should calculate the current total of a hand.

## 4. Player Actions

This component handles the player's decisions.

The player can:

- Choose H to hit and receive another card.
- Choose S to stand.

The program must:

- Only accept H or S as valid commands.
- Ask the player again when invalid input is entered.
- Add a new card to the player's hand after a hit.
- Immediately make the player lose if their hand exceeds 21.

## 5. Dealer Actions

This component controls the dealer.

At the beginning of the round:

- The dealer receives two cards.
- One card is face up.
- One card is face down.

When the player stands:

- Reveal the dealer's hidden card.
- Calculate the dealer's hand value.
- Draw additional cards until the dealer's total is 17 or higher.
- If the dealer's total exceeds 21, the player wins.

## 6. Game Flow

This component controls the complete Blackjack game.

The game should:

1. Create and shuffle the deck.
2. Deal two cards to the player.
3. Deal two cards to the dealer.
4. Show the player's cards and the dealer's up card.
5. Ask the player to hit or stand.
6. Continue the player's turn until they stand or bust.
7. If the player stands, start the dealer's turn.
8. Reveal the dealer's hidden card.
9. Let the dealer draw until reaching 17 or higher.
10. Determine the winner.
11. Display the final hands and outcome.

## 7. Display and User Interaction

Before every player decision, the program must display:

- The player's cards.
- The player's running total.
- The dealer's up card.

At the end of the game, the program must display:

- The player's complete hand.
- The dealer's complete hand.
- The final totals.
- The outcome.

The outcome should be either:

- You won
- Dealer won

## 8. Project Structure

The project should contain separate folders for:

- Blackjack code
- Examples
- Tests

The exact Python files will be determined in Exercise 1.2.

## 9. Testing

After the Blackjack components have been implemented, manually create tests that check:

- Creation of a 52-card deck.
- Correct card values.
- Correct handling of Aces.
- Cards are drawn without replacement.
- Player busting.
- Dealer drawing until reaching at least 17.
- Dealer busting.
- Player winning.
- Dealer winning.
- A tie resulting in a dealer win.
- Invalid player input being rejected.

## 10. Examples

Create two working examples that demonstrate how the Blackjack components can be used.

The examples should be created after the main Blackjack components have been implemented and reviewed.

## 11. Development Order

The project should be developed in the following order:

1. Create the project plan.
2. Create the project structure.
3. Implement the Blackjack components.
4. Manually create tests.
5. Create two working examples.
6. Review the code.