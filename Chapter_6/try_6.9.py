#Done by Carlos Amaral in 23/06/2020

"""
Make a dictionary called favorite_places . Think of three
names to use as keys in the dictionary, and store one to three favorite places
for each person. To make this exercise a bit more interesting, ask some friends
to name a few of their favorite places. Loop through the dictionary, and print
each person’s name and their favorite places.
"""

#Favourite places

favourite_places = {
    'Carlos': ['Porto', 'Aveiro'],
    'Patricia': ['Portimão','Lisboa'],
    'Tereza': ['Prague', 'Wien'],
    }
for name, places in favourite_places.items():
    print(f"\n{name.title()}'s favourite places are: ")

    for place in places:
        print(f"{place.title()}")