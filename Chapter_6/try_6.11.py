#Done by Carlos Amaral in 23/06/2020

"""
Make a dictionary called cities . Use the names of three cities as
keys in your dictionary. Create a dictionary of information about each city and
include the country that the city is in, its approximate population, and one fact
about that city. The keys for each city’s dictionary should be something like
country , population , and fact . Print the name of each city and all of the infor-
mation you have stored about it.
"""

#Cities

cities = []


Porto = {
    'name': 'Porto',
    'country': 'Portugal',
    'population': '1 722 374 inhabitants',
    'nickname': 'Cidade invicta',
    'river': 'Douro',
    }
cities.append(Porto)

Viseu = {
    'name': 'Viseu',
    'country': 'Portugal',
    'population': '66 143',
    'nickname': 'Cidade museu',
    'river': 'Pavia',
    }
cities.append(Viseu)

for city in cities:
    name = f"{city['name']}"
    country = f"{city['country']}"
    population = f"{city['population']}"
    nickname = f"{city['nickname']}"
    river = f"{city['river']}"

    print(f"\nName: {name.title()}")
    print(f"Country: {country.title()}")
    print(f"Population: {population.title()}")
    print(f"Nickname: {nickname.title()}")
    print(f"River: {river.title()}")
    print(f"{name.title()} is a city located in {country.title()} " +
        f"with {population.title()} inhabitants, known has {nickname.title()} " +
        f"and bathed by the {river.title()}. river")






