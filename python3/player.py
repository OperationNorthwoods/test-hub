from card import Card
from deck import Deck

class Player:

    def __init__(self, name):
        self.name = name
        self._hand = []

    def draw(self, deck):
        self._hand.append(deck.deal())

    def show_hand(self):
        return ', '.join([str(card) for card in self._hand])

    def discard(self, card=None, suit=None, rank=None):
        # Flexible discard method can take either a direct card object or a suit and rank parameter.
        if card is not None:
            # The card object is provided directly.
            if card in self._hand:
                self._hand.remove(card)
                print(f'{str(card)} has been discarded.')
            else:
                print('That card is not in your hand')
        elif suit is not None and rank is not None:
            # The suit and rank are provided, so create a Card object.
            try:
                query = Card(suit, rank)
            except ValueError as e:
                print(e)
                return
            for card in self._hand:
                if card.suit == query.suit and card.rank == query.rank:
                    self._hand.remove(card)
                    print(f'{str(card)} has been discarded.')
                    return
            print('That card is not in your hand')
        else:
            # Neither direct card object or suit and rank were provided.
            raise ValueError('You must provide either a Card object or a suit and rank.')


player_one = Player('one')
my_deck = Deck()
player_one.draw(my_deck)
player_one.draw(my_deck)
print(player_one.show_hand())
player_one.discard('diamond', 'ace')
