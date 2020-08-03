#Done by Carlos Amaral in 03/07/2020

"""
Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance.
"""


#Three Restaurants

class Restaurant:
    """Model a restaurant."""

    def __init__ (self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints a summary of the restaurant info."""
        msg = f"{self.restaurant_name} is a {self.cuisine_type} restaurant."
        print(msg)

    def open_restaurant(self):
        """Prints a message indicating the restaurant is open."""
        msg = f"{self.restaurant_name} is now open!"
        print(msg)

the_restaurant = Restaurant('Mercantel', 'cozinha do mar')
porto_restaurant = Restaurant('Foz', 'cozinha portuguesa')
Lx_restaurant = Restaurant('Alcantara', 'comida')


the_restaurant.describe_restaurant()
the_restaurant.open_restaurant()

print("\n")
porto_restaurant.describe_restaurant()
porto_restaurant.open_restaurant()

print("\n")
Lx_restaurant.describe_restaurant()
Lx_restaurant.open_restaurant()