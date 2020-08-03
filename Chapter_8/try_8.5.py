#Done by Carlos Amaral in 28/06/2020

"""
Write a function called describe_city() that accepts the name of
a city and its country. The function should print a simple sentence, such as
Reykjavik is in Iceland . Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in 
the default country.
"""

#Cities

def describe_city(name, country='Portugal'):
    """Displays some information about a city"""
    print(f"{name} is located in {country.title()}.")

describe_city('Porto')
describe_city('Aveiro')
describe_city('Genoa', country='Italy')
