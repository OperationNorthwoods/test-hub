from card import Card
from deck import Deck
from player import Player
import random


# Uses inheritance to make a special card from Card.
class BlackjackCard(Card):
    
    def __init__(self, suit, rank):
        super().__init__(suit, rank)
        if rank in ['jack', 'queen', 'king']:
            self.value = 10
        elif rank == 'ace':
            self.value = 11  # We can handle the '1 or 11' situation when calculating score
        else:
            self.value = int(rank)

# Uses inheritance to make a special deck from Deck.
class BlackjackDeck(Deck):
    def __init__(self, num_decks=1):
        self.num_decks = num_decks
        super().__init__()

    def build(self): # Overrides inherited Deck.build() method.
        self._cards = [BlackjackCard(suit, rank) for _ in range(self.num_decks)
                       for suit in self.suits for rank in self.ranks]
        # if num_decks>1, multiple decks will be contained in one list. This is normal for Blackjack.
        random.shuffle(self._cards)
    
    # BlackjackDeck() tested and working.

# class BlackjackGame:
#     def __init__(self, num_decks=1):
#         self.deck = BlackjackDeck(num_decks)
#         self.players_hand = []
#         self.dealers_hand = []
        
#         # Not sure about this one.
#         def deal_initial_cards(self):
#             self.players_hand.append(self.deck.draw())
#             self.dealers_hand.append(self.deck.draw())
#             self.players_hand.append(self.deck.draw())
#             self.dealers_hand.append(self.deck.draw())

#         # Elegant scorekeeping method for dealing with Aces.
#         def calculate_score(self, hand):
#             score = 0
#             aces = 0

#             for card in hand:
#                 if card.rank == 'ace':
#                     score += 11
#                     aces += 1
#                 else:
#                     score += card.value

#             # if score is over 21 and there is an ace in hand, reduce score by 10
#             while score > 21 and aces:
#                 score -= 10
#                 aces -= 1

#             return score


#          # Implement other methods like player_hit, player_stand, dealer_play etc.

# def main():
    # print('Welcome to Blackjack!')
    # game = BlackjackGame()
    # game.deal_initial_cards()

# Add game logic here - player decisions, dealer decisions, etc.

#
# my_deck = BlackjackDeck(2)
# print(my_deck.length())

# my_card = BlackjackCard(2)
# print(my_card.suit)


#
# if __name__ == "__main__":
#     main()