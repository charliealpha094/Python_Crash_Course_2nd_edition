#Done by Carlos Amaral in 06/07/2020

"""
An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote
in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). Either version of
the class will work; just pick the one you like better. Add an attribute called
flavors that stores a list of ice cream flavors. Write a method that displays
these flavors. Create an instance of IceCreamStand , and call this method.
"""

#Ice cream stand

class Restaurant:
    """A simple attempt to represent a Restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        #Initialize restaurant_name, cuisine_type attributes.
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints information about the restaurant."""
        msg = f"{self.restaurant_name} is a {self.cuisine_type} restaurant."
        print(msg)

    def open_restaurant(self):
        msg = f"{self.restaurant_name} is now open!"
        print(msg)


class IceCreamStand(Restaurant):
    """Represent aspects of a restaurant, specific to ice cream flavours."""

    def __init__(self, restaurant_name, cuisine_type = 'ice cream'):
        """Initialize attributes of the parent class."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = ['magnum', 'calipo', 'perna de pau']


    def get_flavours(self):
        """Show the flavours available."""
        print("The following flavours are available:")
        for flavour in self.flavours:
            print("* " + flavour)

Ice_Stand = IceCreamStand('Secçao fria', 'gelados')
Ice_Stand.describe_restaurant()
Ice_Stand.open_restaurant()
print("\n")
Ice_Stand.get_flavours()
