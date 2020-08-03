#Done by Carlos Amaral in 09/07/2020

"""
Make a class Die with one attribute called sides , which has a default
value of 6. Write a method called roll_die() that prints a random number
between 1 and the number of sides the die has. Make a 6-sided die and roll it
10 times.
Make a 10-sided die and a 20-sided die. Roll each die 10 times.
"""

#Dice

#6-sided Die.
from random import randint

class Die():
    """A simple attempt to model a dice."""

    def __init__(self, sides=6):
        """Initialize die attributes."""
        self.sides = sides

    def roll_die(self):
        """Print a random number between 1 and 6."""
        print(randint(1, self.sides))


print("6 sided Die")
#Build a 6-sided Die
d6 = Die(sides=6)

results = ''
#Make it roll 10 times
for roll in range(10):
    result = d6.roll_die()

print(results)



print("\n")
print("10 sided Die")


#10-sided Die.
from  random import randint

class Die():
    """A simple attempt to represent a Dice."""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))


#Make a 10 sided die.
d = Die(sides=10)

result = ''
#Make it roll 10 times
for roll in range(10):
    result = d.roll_die()
print(results)




print("\n")

print("20 sided Dice")

from random import randint

class Die():
    """A simple attempt to model a Dice."""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))

#Build a 20 sided Die.
d20 = Die (sides=20)

#Make it roll 10 times

result = ''
for roll in range(10):
    result = d20.roll_die()
print(results)