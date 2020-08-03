#Done by Carlos Amaral in 05/07/2020

#Restaurant

class Restaurant:
    """An attempt to model a Restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name and cuisine_type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints information about the restaurant."""
        print(f"\n{self.restaurant_name}")

    def open_restaurant(self):
        """Prints a message that the restaurant is open."""
        print(f"\n{self.restaurant_name} is now open!")

restaurant = Restaurant('Mercantel', 'cozinha portuguesa')

print(f"The restaurant's name is {restaurant.restaurant_name}" +
      f" and is a {restaurant.cuisine_type} restaurant.")

print(f"The {restaurant.restaurant_name} is now open!")

restaurant.describe_restaurant()
restaurant.open_restaurant()