# Useful stuff from random module.

import random                                       # Imports random module.

x = random.randint(1,6)                             # Sets var 'x' as a random number between 1 and 6.
y = random.random()                                 # Sets var 'y' as a random number between 0 and 1.

myList = ["rock","paper","scissors"]                # Defines a list with three items.
z = random.choice(myList)                           # Defines Z as a random item from the list.

cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]         # Creates a list with numbers and letters.
random.shuffle(cards)                               # Orders the list randomly.

print(x)
print(y)
print(z)
print(cards)