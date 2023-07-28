from card import Card
from deck import Deck
from player import Player
import blackjack as Blackjack

# make example code that illistrates the functions of your program so its easier to come back too after a long break


print('card.py') # card.py
my_card = Card("hearts", "6")
print(my_card)
print(my_card.suit)
print(my_card.rank)
# my_card.rank = "15" # error will be raised
print(my_card)


print('===+++===\ndeck.py') # deck.py
my_deck = Deck()
print(my_deck)
print('========================================================')
print(my_deck)
for i in range(0,52):
    print(Deck.deal(my_deck))
Deck.is_Present(my_deck, 'diamonds', '8')


print('===+++===\nplayer.py') # player.py
player_one = Player('one')
my_deck = Deck()
player_one.draw(my_deck)
player_one.draw(my_deck)
print(player_one.show_hand())
player_one.discard(None, 'diamond', 'ace')