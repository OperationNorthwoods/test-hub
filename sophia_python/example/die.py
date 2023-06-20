# Importing the randint module
from random import randint

# The class Die implements a six sided die
class Die:
    # The __init__ method is used to create a new instance of die with a default value of 1
    def __init__(self):
        self.value = 1

    # The roll method is used to set the value to a random number between 1 and 6
    def roll(self):
        self.value = randint(1, 6)

    # The getValue method returns the top face value of the die
    def getValue(self):
        return self.value

    # The __str__ method returns the string representation of the value of the die
    def __str__(self):
        return str(self.getValue())
