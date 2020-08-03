#Done by Carlos Amaral in 23/06/2020

"""
Modify your program from Exercise 6-2 (page 99)
so each person can have more than one favorite number. Then print each per-
son’s name along with their favorite numbers.
"""

#Favourite Numbers

favourite_numbers = {
    'Carlos': ['17', '7'],
    'Patricia': ['12', '7'],
    'Rita': ['23', '2'],
    'Sofia': ['2', '45'],
    'Eva': ['15', '25'],
    'Tereza': ['24', '41'],
    }

for name, numbers in favourite_numbers.items():
    print(f"\n{name.title()}'s favourite number is:")
    for number in numbers:
        print(number.title())
