#Done by Carlos Amaral in 04/07/2020

"""
Make a class called User . Create two attributes called first_name
and last_name , and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user.
"""


#Users

class User:
    """A class that represents a User."""

    def __init__(self, first_name, last_name, username, email, phone_no):
        """Initialize first name and last name attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.phone_no = phone_no

    def describe_user(self):
        """Prints a summary of the user's information."""
        print(f"{self.first_name} {self.last_name}"
                f"\nUsername:  {self.username}"
                f"\nEmail: {self.email}"
                f"\nPhone number: {self.phone_no}")

    def greet_user(self):
        """Prints a greeting to the user."""
        msg = f"\nWelcome {self.username}!"
        print(msg)

charlie = User('Carlos', 'Amaral', 'charliealpha094', 
               'carlosamaral94@gmail.com', 916165804)

Tereza = User('Tereza', 'Srbova', 'TerezaS', 
              'terezasrbova87@gmail.com', 917389765)

charlie.describe_user()
charlie.greet_user()

print("\n")

Tereza.describe_user()
Tereza.greet_user()
