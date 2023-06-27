from card import Card
import random

class Deck:
    suits = ('clubs','diamonds','hearts','spades')
    ranks = ('2','3','4','5','6','7','8','9','10','jack','queen','king','ace')

    def __init__(self):
        self._cards = []
        self.build()
    
    def __str__(self):
        return ', '.join([str(card) for card in self._cards])

    def build(self):
        self._cards = [Card(s, r) for s in self.suits for r in self.ranks]
        random.shuffle(self._cards)
    
    def length(self):
        return len(self._cards)
    
    def deal(self):
        return self._cards.pop(0)

    def is_Present(self, suit, rank):
        query = str(Card(suit, rank))
        for card in self._cards:
            index = self._cards.index(card)
            if str(card) == query:
                print('Yes, the ' + str(card))
                print(f'Card is present at position {index}.')
                return
                
# my_deck = Deck()
# print(my_deck)

# Deck.shuffle(my_deck)
# print('========================================================')
# print(my_deck)

# for i in range(0,52):
#     print(Deck.deal(my_deck))

# Deck.isPresent(my_deck, 'diamonds', '8')