#Done by Carlos Amaral in 29/06/2020

"""
Write a function called city_country() that takes in the name
of a city and its country. The function should return a string formatted 
like this: "Santiago, Chile".
Call your function with at least three city-country pairs, and print the
values that are returned.
"""


#City Names

def city_country(city, country):
    """Return the the name of a city and it's country."""
    place = f"{city}, {country}"
    return place.title()

city = city_country('Porto', 'Portugal')
city2 = city_country('Aveiro', 'Portugal')
city3 = city_country('Genoa', 'Italy')
print(city)
print(city2)
print(city3)