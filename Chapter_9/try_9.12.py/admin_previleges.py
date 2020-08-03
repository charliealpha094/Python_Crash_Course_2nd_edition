#Done by Carlos Amaral in 08/07/2020

"""
Store the User class in one module, and store the
Privileges and Admin classes in a separate module. In a separate file, create
an Admin instance and call show_privileges() to show that everything is still
working correctly.
"""

from User2 import User

class Admin(User):
    """Represents aspects of an user, specific to administrators."""

    def __init__(self, first_name, last_name, username, email, phone_no):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an administrator
        """

       

        super().__init__(first_name, last_name, username, email, phone_no)
        self.previleges = ['can add post', 'can delete post', 'can ban user']

    def show_previleges(self):
        print("\nAdministrator has the following previleges:")
        """Prints the previleges of the admin."""
        for previlege in self.previleges:
            print("-" + previlege)

