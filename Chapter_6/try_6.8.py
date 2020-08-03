#Done by Carlos Amaral in 23/06/2020

"""
Make several dictionaries, where each dictionary represents a differ-
ent pet. In each dictionary, include the kind of animal and the owner’s name.
Store these dictionaries in a list called pets . Next, loop through your list and as
you do, print everything you know about each pet.
"""

#Pets

pets = []



Junior = {
    'name': 'Junior',
    'owner': 'Sr.Alberto',
    'kind_animal': 'dog',
    }
pets.append(Junior)

Dick = {
    'name': 'Dick',
    'owner': 'Sr.Osvaldo',
    'kind_animal': 'dog',
    }
pets.append(Dick)

Ninocas = {
    'name': 'Ninocas',
    'owner': 'Carlos',
    'kind_animal': 'hamster',
    }
pets.append(Ninocas)

for pet in pets:
    name = f"{pet['name']}"
    owner = f"{pet['owner']}"
    kind_animal = f"{pet['kind_animal']}"

    print(f"\nName: {name.title()}")
    print(f"Owner: {owner.title()}")
    print(f"Kind_animal: {kind_animal.title()}")
    print(f"{name.title()} is a {kind_animal.title()} and is owned by " +
       f"{owner.title()}." )