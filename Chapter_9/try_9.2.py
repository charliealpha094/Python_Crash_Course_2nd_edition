#Done by Carlos Amaral in 03/07/2020

"""
Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance.
"""

#Three restaurants

class Restaurant:
    """A class that represents a Restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine attributes."""
        self.restaurant_name = restaurant_name
        self. cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints information about the restaurant."""
        print(f"{self.restaurant_name}")

    def open_restaurant(self):
        """Prints a message that the restaurant is open."""
        print(f"\n{self.restaurant_name} is open!")

the_restaurant = Restaurant('Mercantel', 'cozinha portuguesa')
porto_restaurant = Restaurant('Foz', 'cozinha do mar')
Lx_restaurant = Restaurant('Alcantara', 'comida')

print(f"My main restaurant's name is {the_restaurant.restaurant_name}.")
print(f"It's a {the_restaurant.cuisine_type} restaurant.")
the_restaurant.describe_restaurant()


print(f"\nMy other restaurant is {porto_restaurant.restaurant_name}.")
print(f"{porto_restaurant.restaurant_name} is {porto_restaurant.cuisine_type}!")
porto_restaurant.open_restaurant()


print(f"\nMy Lisbon restaurant is {Lx_restaurant.restaurant_name}.")
print(f"It serves {Lx_restaurant.cuisine_type}!")
Lx_restaurant.describe_restaurant()