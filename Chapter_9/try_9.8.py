#Done by Carlos Amaral in 07/07/2020

"""
Write a separate Privileges class. The class should have one
attribute, privileges , that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class. Make a Privileges instance
as an attribute in the Admin class. Create a new instance of Admin and use your
method to show its privileges.
"""

#Previleges

class User:
    """A simple attempt to represent a user."""

    def __init__(self, first_name, last_name, username, email, phone_no):
        """Initialize attributes to describe a user."""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.phone_no = phone_no

    def describe_user(self):
        """Prints information about the user."""
        print(f"{self.first_name} {self.last_name}"
               f"\nUsername: {self.username}"
               f"\nEmail: {self.email}"
               f"\nPhone: {self.phone_no}")

    def greet_user(self):
        """Prints a greeting to the user."""
        print(f"\nWelcome {self.username}!")


class Admin(User): 
    """Represents aspects of a user, specific to the previleges of an admin."""

    def __init__(self, first_name, last_name, username, email, phone_no):
        """Initializes the attributes of the parent class."""
        super().__init__(first_name, last_name, username, email, phone_no)
        self.previleges = Previleges()

class Previleges():

    def __init__(self, previleges = []):
        self.previleges = previleges

    def show_previleges(self):
        print("The administrator has the following previleges:")
        if self.previleges:
            for previlege in self.previleges:
                print("-" + previlege)
            else:
                print(f"\nThis user has no previleges!")


administrador = Admin('Carlos', 'Amaral', 'charliealhpa094',
                   'carlosamaral94@gmail.com', 916165804)

administrador.describe_user()
administrador.greet_user()

print("\n")


admin_previleges = ['can add post',
                    'can delete post',
                    'can ban user']

administrador.previleges.previleges = admin_previleges
administrador.previleges.show_previleges()
