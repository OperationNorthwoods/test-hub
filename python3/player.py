from card import Card
from deck import Deck

class Player:
    all_players = []

    def __init__(self, name):
        self.name = name
        Player.all_players.append(self)
        self._hand = None
        self.hand = []
    
    def __del__(self):
        if player in Player.all_players:
            Player.all_players.remove(self)

    def removePlayer(self):
        Player.all_players.remove(self)

    def __str__(self):
        return "Player name: " + self.name
    
    @property
    def hand(self):
        return self._hand
    # Getter must be defined before the Setter, otherwise Error is thrown.
    @hand.setter
    def hand(self, cards):
        if all(isinstance(card, Card) for card in cards):
            self._hand = cards
        else:
            raise ValueError("hand should be a list of Card objects")
        # Input validation.


    def draw(self, deck):
        self._hand.append(deck.deal())

    def add_card(self, card):
        if not isinstance(card, Card):
            raise ValueError("The provided object is not an instance of the Card class.")
        self._hand.append(card)
        # for testing only, logic will need to be added to manage cards on the deck side

    def show_hand(self):
        return ', '.join([str(card) for card in self._hand])

    def discard(self, card=None, suit=None, rank=None): # If not using explicit parameter values (ie suit='x' and rank='y') you must place None for the first argument.
        # IE: `player_one.discard('diamond', 'ace')` < WRONG. This will fail to trigger the proper if statement/Card() obj input validaiton.
        # IE: `player_one.discard(None, 'diamond', 'ace')` < Perfect.
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
                print(f"Created card: {query}")
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


# player_one = Player('one')
# my_deck = Deck()
# player_one.draw(my_deck)
# player_one.draw(my_deck)
# print(player_one.show_hand())
# player_one.discard(None, 'diamond', 'ace')
player1 = Player('poop')
player2 = Player('fart')
# for player in Player.all_players:
#     print(player)
# player2.removePlayer()
# for player in Player.all_players:
#     print(player)
for player in Player.all_players:
    player.draw()