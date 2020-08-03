#Done by Carlos Amaral in 08/07/2020

"""
Start with your work from Exercise 9-8 (page 173).
Store the classes User , Privileges , and Admin in one module. Create a sepa-
rate file, make an Admin instance, and call show_privileges() to show that
everything is working correctly.
"""

#Imported Admin

class User:
    """A simple attempt to represent an User."""

    def __init__(self, first_name, last_name, username, email, phone_no):
        """Initialize attributes of a user."""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.phone_no = phone_no

    def describe_user(self):
        """Prints information about the user."""
        print(f"{self.first_name} {self.last_name} is the administrator!"
              f"\nUsername: {self.username}"
              f"\nEmail: {self.email}"
              f"\nPhone: {self.phone_no}")

    def greet_user(self):
        """Prints a greeting to the user."""
        print(f"\nWelcome {self.username}!")


class Admin(User):
    """Represents aspects of aspects of a User, specific to an Administrator."""

    def __init__(self, first_name, last_name, username, email, phone_no):
        """Initialize attributes of the parent class."""
        super().__init__(first_name, last_name, username, email, phone_no)
        self.previleges = ['can add post', 'can delete post', 'can ban user']

    def show_previleges(self):
        """Show the administrator previleges."""
        print("\nThe administrator has the following previleges:")
        for previlege in self.previleges:
            print("-" + previlege)
