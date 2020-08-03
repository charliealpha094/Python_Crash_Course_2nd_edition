#Done by Carlos Amaral in 07/07/2020

"""
Using your latest Restaurant class, store it in a mod-
ule. Make a separate file that imports Restaurant . Make a Restaurant instance,
and call one of Restaurant ’s methods to show that the import statement is work-
ing properly.
"""

#Imported Restaurant

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