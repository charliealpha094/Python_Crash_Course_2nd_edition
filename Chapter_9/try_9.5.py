#Done by Carlos Amaral in 06/07/2020

"""
Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 162). Write a method called increment_login
_attempts() that increments the value of login_attempts by 1. Write another
method called reset_login_attempts() that resets the value of login_attempts
to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts() . Print login_attempts again to
make sure it was reset to 0.
"""

#Loggin Attempts

class User:
    """A class that represents a user."""

    def __init__(self, first_name, last_name, username, email, phone_no):
        """Initialize information data attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.phone_no = phone_no
        self.login_attempts = 0

    def describe_user(self):
        """Prints a summary of the user's information."""
        print(f"\n{self.first_name} {self.last_name}"
              f"\nUsername: {self.username}"
              f"\nEmail: {self.email}"
              f"\nPhone no.: {self.phone_no}")

    def greet_user(self):
        """Prints a greeting to the user."""
        print(f"Welcome {self.username}!")

    def increment_login_attempts(self, increment):
        """Increments the value of login attempts by 1."""
        self.login_attempts += increment

    def reset_login_attempts(self):
        """Resets the value of login attempts to 0."""
        self.login_attempts = 0

charlie = User('Carlos', 'Amaral', 'charliealpha094',
                'carlosamaral94@gmail.com', 916165804)

Tereza = User('Tereza', 'Srbova', 'TerezaS', 
               'terezasrbova87@gmail.com', 917389765)

charlie.describe_user()
charlie.greet_user()

Tereza.describe_user()
Tereza.greet_user()

print(f"\nCharlie Login attempts: {charlie.login_attempts}")
charlie.increment_login_attempts(1)
print(f"Charlie Login attempts: {charlie.login_attempts}")
charlie.increment_login_attempts(1)
print(f"Charlie Login attempts: {charlie.login_attempts}")
charlie.increment_login_attempts(1)
print(f"Charlie Login attempts: {charlie.login_attempts}")

print("\nReseting login attempts...")
charlie.reset_login_attempts()
print(f"Charlie Login attempts: {charlie.login_attempts}")