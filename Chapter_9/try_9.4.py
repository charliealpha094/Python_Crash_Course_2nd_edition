#Done by Carlos Amaral in 04/07/2020

"""
Start with your program from Exercise 9-1 (page 162).
Add an attribute called number_served with a default value of 0. Create an
instance called restaurant from this class. Print the number of customers the
restaurant has served, and then change this value and print it again.
Add a method called set_number_served() that lets you set the number
of customers that have been served. Call this method with a new number and
print the value again.
"""

#Number served

class Restaurant:
    """An attempt to model a restaurant."""

    def __init__(self, restaurante_name, cuisine_type):
        self.restaurante_name = restaurante_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Prints information about the restaurant."""
        msg = f"{self.restaurante_name} is a {self.cuisine_type} restaurant."
        print(msg)

    def open_restaurant(self):
        """Prints a message indicating the restaurant is open."""
        msg = f"{self.restaurante_name} is now open!!"
        print(msg)

    def set_number_served(self, number_served):
        """Ability to set the number the costumers that've been served."""
        self.number_served = number_served
        
    def increment_number_served(self, increment):
        """Ability to increment the no. of costumers that've been served."""
        self.number_served += increment

restaurant = Restaurant('Mercantel', 'cozinha')
restaurant.describe_restaurant()
restaurant.open_restaurant()

print(f"\nRestaurant has served: {restaurant.number_served} costumers.")
restaurant.number_served = 34
print(f"Restaurant has served: {restaurant.number_served} costumers.")

restaurant.set_number_served(100)
print(f"Restaurant has served: {restaurant.number_served} costumers.")

restaurant.increment_number_served(222)
print(f"Restaurant has served: {restaurant.number_served} costumers.")


