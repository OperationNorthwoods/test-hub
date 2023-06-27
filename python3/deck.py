from card import Card
import random

class Deck:

    def __init__(self):
        self._cards = []
        self.populate()
    
    def __str__(self):
        return ', '.join([str(card) for card in self._cards])

    def populate(self):
        suits = ('clubs','diamonds','hearts','spades')
        ranks = ('2','3','4','5','6','7','8','9','10','jack','queen','king','ace')
        
        self._cards = [Card(s, r) for s in suits for r in ranks]
    
    def shuffle(self):
        random.shuffle(self._cards)

    def isPresent(self, suit, rank):
        query = str(Card(suit, rank))
        for card in self._cards:
            index = self._cards.index(card)
            if str(card) == query:
                print('Yes, the ' + str(card))
                print(f'Card is present at position {index}.')
                return
                
                
my_deck = Deck()

# print(my_deck)

# Deck.shuffle(my_deck)
# print('========================================================')
# print(my_deck)

Deck.isPresent(my_deck, 'diamonds', '8')