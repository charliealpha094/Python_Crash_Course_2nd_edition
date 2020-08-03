#Done by Carlos Amaral in 08/07/2020

"""
Store the User class in one module, and store the
Privileges and Admin classes in a separate module. In a separate file, create
an Admin instance and call show_privileges() to show that everything is still
working correctly.
"""

#Multiple Modules

class User:
    """A simple attempt to represent an User."""

    def __init__(self, first_name, last_name, username, email, phone_no):
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

    def greeting_user(self):
        """Prints a greeting to the user."""
        print(f"\nWelcome {self.username}!")