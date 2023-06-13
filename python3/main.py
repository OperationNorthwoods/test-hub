from card import Card
import random

suits = ('clubs','diamonds','hearts','spades')
ranks = ('2','3','4','5','6','7','8','9','10','jack','queen','king','ace')

'''
def createDeck():
    deck = range(1,52)
    card = C
    for card in Card:
'''
def randomize(x):
    randSuit = random.randint(0,3)
    randRank = random.randint(0,12)
    if x == 'suit':
        return suits[randSuit]
    elif x == 'rank':
        return ranks[randRank]
    elif x == 'both':
        return suits[randSuit], ranks[randRank]
    else:
        raise ValueError("Invalid argument")
    
print(randomize('suit'))
print(randomize('rank'))    
a,b = randomize('both')
print(a)
print(b)