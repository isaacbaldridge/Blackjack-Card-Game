# Blackjack Card Game
This is my second project built using Python3. I used this project as an opportunity to become more familiar with Python syntax (coming from a JS background), and also to gain exposure to object-oriented programming. Not to mention learning a new card game is always a fun time! :)

If you already know how to play, feel free to skip to the Set-Up section.

## How to Play
### Goal to win
Add the numerical values of your cards up so that they equal 21, OR are closer to 21 than your opponent.
### Card values
All numerbered cards are equal in value to their numerical rank. Suit has no impact on value.
Example:
```
2 of Hearts: Value = 2
2 of Diamonds: Value = 2
3 of Spades: Value = 3
8 of Clubs: Value = 8
```

Jack, Queen, and King all have a value of 10. Suit has not impact on value.
```
Jack of Hearts: Value = 10
Queen of Spades: Value = 10
King of Clubs: Value = 10
```
Aces will have a value of either 11 or 1, whichever is better for the player. Suit has no impact on value. More on this in the next section.

### Game Loop
After choosing the number of games to play, the player and dealer will be dealt two cards from the deck. Only one of the dealer's cards will visible to the player, the other card will be hidden. The value of the player's hand will be calculated by adding the values of the two cards the player currently has in their hand. Depending on how close the value is to 21, the player can choose to Hit, or Stand.

#### Hit
The player chooses to be dealt a third card from the deck. The value of the third card will be added to values of the other two. Choosing this option can be beneficial or risky, depending on what the player's first two cards are. Let's look at some examples.

##### Beneficial scenario
```
Player's initial hand
4 of Diamonds
5 of Hearts
Player's hand value = 9
```
Because 9 is so low and not at all close to 21, it makes sense for the player to Hit.

```
Player's new hand
4 of Diamonds
5 of Hearts
Ace of Spades
Player's new hand value = 20
```
The player drew an ace! An ace can have a value of either 11 or 1, whichever is better for the player.

```
Ace value = 11
Player's potential hand value = 4 + 5 + 11 = 20

Ace value = 1
Player's opotential hand value = 4 + 5 + 1 = 10
```
When the ace value = 11, the player's new hand value is 20, which is less than 21, but very close! The only way for the player to lose is if the dealer's hand value is equal to 21, which is possible, but unlikely. When the ace value = 1, the player's new hand value is 10, which is still not very close to 21; the likelihood that the dealer's hand value is closer to 21 than the player's is relatively high.

##### Risky scenario (bad outcome)
```
Player's initial hand
8 of Spades
9 of Clubs
Player's hand value = 17
```
Because the player's hand value is relatively close to 21, it is risky to Hit. If the third card puts the player's hand value over 21, the player loses.

```
Player's new hand
8 of Spades
9 of Clubs
6 of Hearts
Player's hand value = 23
```
The third card puts the player's hand value over 21, so they lose! This is called busting.

##### Risky scenario (good outcome)
While it is unlikely, the player can still win by Hitting when their initial hand value is close to 21. It just depends on how lucky you feel. Can you beat the odds?
```
Player's initial hand
Jack of Clubs
9 of Hearts
Player's hand value = 19
```
The player is so close to 21, that choosing to Hit puts them at a high risk of busting. But they are feeling lucky.

```
Player's new hand
Jack of Clubs
9 of Hearts
Ace of Diamonds
Player's new hand value = 20
```
In this scenario, the player drew an ace, which can have a value of 11 or a value of 1, whichever is better for the player. In this case, a value of 1 is better, because it keeps the player's hand value under 21. If the ace value was 11, the player would bust.

#### Stand
Sometimes, it is better to play it safe instead of risking your hand with a Hit. In this case, the player can Stand. The player simply chooses to skip their turn and allow the dealer their chance to Hit or Stand. While standing can be a safer option, there are still beneficial and risky scenarios to explore.

##### Beneficial scenario
Let's take a look at the player's initial hand from the previous example (Hit risky scenario (good outcome)), but this time, we will also include the dealer's hand from the player's perspective.
```
Player's initial hand
Jack of Clubs
9 of Hearts
Player's hand value = 19
```

```
Dealer's hand
5 of Clubs
Unknown card
Dealer's maximum possible hand value = 16
```
We saw what the good outcome of the risky scenario could look like, but it is still an unlikely occurrance. It makes better sense in this scenario to Stand, and keep the player's hand value at 19. We don't know what the dealer's second card is, but we do know that at most, the dealer's hand value is 16 (if the dealer's other card is an ace with value = 11). The dealer can choose to Hit, but they can only win against the player if their final hand value equals 20 or 21 (higher than player's value = 19). This is unlikely, and it is more likely that the dealer will either bust (go over 21), or will still end with a hand value lower than the player's.

##### Risky scenario

The player may find themselves in a position similar to the dealer in the previous example.

```
Player's hand
5 of Hearts
Jack of Spades
Player's initial hand value = 15
```
If the player chooses to Stand in this scenario, they risk losing out on a better hand than if they chose to Hit. It is relatively likely that the dealer could already have a better initial hand, so if the player Stands, they essentially surrender their win. Alternatively, the dealer might have a worse hand, but after the player chooses to Stand, the dealer could choose to Hit, thereby increasing their hand's value to surpass the player's.

However, if the player chose to Hit, they also risk the possibility of increasing their hand value over 21 and busting. When the player receives an initial hand value like the example above, sometimes all bad outcomes of risky scenarios are equally likely (or close to it), so the decision becomes more difficult. In the end, it is a game of luck, so follow your gut. :)

##### Automatic win
If either the player or the dealer receive an Ace (value = 11) and one of the royal cards (Jack, Queen, King) (value = 10), then their hand value is automatically calculated to be 21, so they automatically win the game!

## Set-Up
0.) Ensure that you have [Python installed](https://realpython.com/installing-python/#how-to-install-from-the-full-installer) on your machine.

1.) Fork the repo and clone it down using the SSH key. Copy and paste code below in your preferred directory in your terminal.
`git clone git@github.com:isaacbaldridge/Blackjack-Card-Game.git`

2.) Run the main.py file.

3.) You will be prompted in the terminal to enter the number of games you wish to play. Use integers.

4.) The rest of the game, you will be prompted to choose the "Hit" or "Stand" options.
