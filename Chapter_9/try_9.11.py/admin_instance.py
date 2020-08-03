#Done by Carlos Amaral in 08/07/2020

"""
Start with your work from Exercise 9-8 (page 173).
Store the classes User , Privileges , and Admin in one module. Create a sepa-
rate file, make an Admin instance, and call show_privileges() to show that
everything is working correctly.
"""

from admin import Admin

administrador = Admin('Carlos', 'Amaral', 'charliealpha094',
                      'carlosamaral94@gmail.com', 916165804)

administrador.describe_user()
administrador.greet_user()

administrador.show_previleges()