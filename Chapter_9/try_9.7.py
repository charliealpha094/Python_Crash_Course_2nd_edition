#Done by Carlos Amaral in 07/07/2020

"""
An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 162)
or Exercise 9-5 (page 167). Add an attribute, privileges , that stores a list
of strings like "can add post" , "can delete post" , "can ban user" , and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin , and call your method.
"""


#Admin

class User():
    """A simple attempt to represent a few users."""

    def __init__(self, first_name, last_name, username, email, phone_no):
        """Initialize first, last names, username, email and phone number."""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.phone_no = phone_no

    def describe_user(self):
        """Prints the information about the users."""
        print(f"{self.first_name} {self.last_name} is the administrator!"
             f"\nUsername: {self.username}"
             f"\nEmail: {self.email}"
             f"\nPhone: {self.phone_no}")

    def greet_user(self):
        """Prints a greeting to the users."""
        print(f"\nWelcome {self.username}!")


class Admin(User):
    """Represents aspects of a user, specific to previleges of an admin."""

    def __init__(self, first_name, last_name, username, email, phone_no):
        """Initializes attributes of the parent class."""
        super().__init__(first_name, last_name, username, email, phone_no)
        self.previleges = ['can add post', 'can delete post', 'can ban user']

    def show_previleges(self):
        """Show the admin previleges."""
        print("The administrator has the following previleges:")
        for previlege in self.previleges:
            print("-" + previlege)

administrador = Admin('Carlos', 'Amaral', 'charliealpha094', 
                      'carlosamaral94@gmail.com', 916165804)

administrador.describe_user()
administrador.greet_user()
print("\n")
administrador.show_previleges()





