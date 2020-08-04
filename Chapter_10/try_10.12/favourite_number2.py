#Done by Carlos Amaral in 14/07/2020


#Favourite Number Remembered

"""
Combine the two programs from
Exercise 10-11 into one file. If the number is already stored, report the favorite
number to the user. If not, prompt for the user’s favorite number and store it in a
file. Run the program twice to see that it works.
"""

import json

filename = 'favourite_number.json'

try:
    with open(filename) as file:
        favourite_number = json.load(file)
except FileNotFoundError:
    favourite_number = input("What is your favourite number? ")
    with open(filename, 'w') as file:
        json.dump(favourite_number, file)
        print(f"I'll remember your favourite number. It's {favourite_number}!")
else:
    print(f"I know your favourite number! It's {favourite_number}!")