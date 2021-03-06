#Done by Carlos Amaral in 16/07/2020

"""
Write a function that accepts two parameters: a city name
and a country name. The function should return a single string of the form
City, Country , such as Santiago, Chile . Store the function in a module called
city _functions.py.
Create a file called test_cities.py that tests the function you just wrote
(remember that you need to import unittest and the function you want to test).
Write a method called test_city_country() to verify that calling your function
with values such as 'santiago' and 'chile' results in the correct string. Run
test_cities.py, and make sure test_city_country() passes.
"""

#City, country

from city_functions import get_formatted_place

print("(Enter 'q' to quit)")

while True:
    city = input("Please, insert a city: ")
    if city == 'q':
        break

    country = input("Please, insert a country: ")
    if country == 'q':
        break

    formatted_place = get_formatted_place(city, country)
    print(f"Place: {formatted_place}")