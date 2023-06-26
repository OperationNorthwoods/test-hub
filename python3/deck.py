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
    
    # def shuffle <<< figure this out next

my_deck = Deck()

print(my_deck)