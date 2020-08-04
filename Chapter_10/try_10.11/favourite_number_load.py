#Done by Carlos Amaral in 14/07/2020


#Favourite number

"""Write a program that prompts for the user’s favorite
number. Use json.dump() to store this number in a file. Write a separate pro-
gram that reads in this value and prints the message, “I know your favorite
number! It’s _____.”
"""

import json

filename = 'favourite_number.json'

with open(filename) as file:
    favourite_number = json.load(file)
    print(f"I know your favourite number! It's {favourite_number}!")
