class Card:

    suits = ('clubs','diamonds','hearts','spades')
    ranks = ('2','3','4','5','6','7','8','9','10','jack','queen','king','ace')

    def __init__(self, suit, rank):
        self._suit = None
        self.suit = suit

        self._rank = None
        self.rank= rank
        # Calls setters which perform input validation when creating card object.

    # This returns a custom string when my_card (obj of Card()) is called, instead of the default object reference
    def __str__(self):
        return f'{self.rank} of {self.suit}'
 
    @property # This transforms this funciton into an attribute, no () are needed to access it.
    def suit(self):
        return self._suit
    # ^^ this is a getter ^^

    @suit.setter
    def suit(self, suit):
        if suit in self.suits:
            self._suit = suit
        else:
            raise ValueError(f"Invalid suit. Choose from {self.suits}")
    # ^^ this is a setter ^^

    @property
    def rank(self):
        return self._rank
    
    @rank.setter
    def rank(self, rank):
        if rank in self.ranks:
            self._rank = rank
        else:
            raise ValueError(f"Invalid suit. Choose from {self.ranks}")


# my_card = Card("hearts", "6")

# print(my_card)

# print(my_card.suit)
# print(my_card.rank)

# my_card.rank = "15"

# print(my_card)