#Done by Carlos Amaral in 28/06/2020

"""
Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different
message.
"""

#Large Shirts

def make_shirts(message, size_shirt = 'large shirt'):
    """Displays information about size and text of a message."""
    print(f"I want a {size_shirt}.")
    print(f"I want to see '{message}' written on my {size_shirt.title()}. ")

make_shirts(message = 'I love python')
make_shirts(size_shirt = 'medium shirt', message= 'I  love python' )
make_shirts(size_shirt = 'small shirt', message= 'Python is cool')

#or

print("\n")

#2nd Version- The most correct one!!!
def make_shirts(message = 'I love python', size_shirt = 'large shirt'):
    """Displays information about size and text of a message."""
    print(f"I want a {size_shirt}.")
    print(f"I want to see '{message}' written on my {size_shirt.title()}. ")

make_shirts()
make_shirts(size_shirt = 'medium shirt')
make_shirts(size_shirt = 'small shirt', message = 'Python is cool')