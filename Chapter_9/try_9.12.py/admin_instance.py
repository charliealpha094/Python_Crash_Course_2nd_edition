#Done by Carlos Amaral in 08/07/2020

"""
Store the User class in one module, and store the
Privileges and Admin classes in a separate module. In a separate file, create
an Admin instance and call show_privileges() to show that everything is still
working correctly.
"""


from User2 import User
from admin_previleges import Admin 

administrador = Admin('Carlos', 'Amaral', 'charliealpha094',
                    'carlosamaral94@gmail.com', 916165804)


administrador.describe_user()
administrador.greeting_user()

administrador.show_previleges()