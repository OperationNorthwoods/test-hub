# The player class is to simulate what a player is able to do. 
# We will first import the class Die that we have created
from die import Die

# The class Player is the functionality that makes use of the Die class.
class Player(object):
    # The __init__ method will create a pair of dice and initialize the other variables.
    def __init__(self):
        self.firstDie = Die() 
        self.secondDie = Die()
        self.roll = ""
        self.rollsCount = 0 
        self.startOfGame = True 
        self.winner = self.loser = False

    # The getNumberOfRolls will return the rollCount for the number of rolls
    def getNumberOfRolls(self):
        return self.rollsCount

    # The rollDice rolls both of the dice once.
    # Then it updates the roll, the won and the lost outcomes. 
    # Lastly it returns a tuple of the values of the dice.
    def rollDice(self):
        # Increment rollCount by 1
        self.rollsCount += 1
        # Roll both dice
        self.firstDie.roll()
        self.secondDie.roll()
        # Set the tuple based on the values from each dice
        (v1, v2) = (self.firstDie.getValue(), self.secondDie.getValue())
        # Set the roll value to the value of the two dice
        self.roll = str((v1, v2)) + " total = " + str(v1 + v2)

        # The logic of the game is now running, if this is the first game
        if self.startOfGame:
            # Initial value is set to the the value of the two dice
            self.initialSum = v1 + v2 
            self.startOfGame = False
            # If the initial sum is equal to 2, 3 or 12, the player is set to have lost
            if self.initialSum in (2, 3, 12):
                self.loser = True
            # If the initial sum is equal to 7 or 11, the player is set to have won
            elif self.initialSum in (7, 11):
                self.winner = True
        # If this is not the first game
        else:
            # We are now checking for the later sum of the values
            laterSum = v1 + v2
            # if it's not the start of the game and a 7 is rolled, the player loses
            if laterSum == 7:
                self.loser = True
            # If the player rolled the same sum as the first sum, the player wins
            elif laterSum == self.initialSum:
                self.winner = True
        return (v1, v2)

    # Returns True if the player has won
    def isWinner(self):
        """Returns True if player has won."""
        return self.winner

    # Returns True if the player has lost
    def isLoser(self):
        """Returns True if player has lost."""
        return self.loser

    # With the game, it's possible that both isWinner and isLower is false
    # If this is the case, the game is not finished and we must roll again until one is true.
    # Plays a full game and counts the rolls for that game. 
    # This returns True for a win and False if the player loses 
    def play(self):
        # We continue to roll as long as both are False
        while not self.isWinner() and not self.isLoser():
            self.rollDice()
        return self.isWinner()

    # The __str__ method will return the last roll as a string.
    def __str__(self):
        """Returns a string representation of the last roll."""
        return self.roll
