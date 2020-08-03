#Done by Carlos Amaral in 28/06/2020

"""
Write a function called make_shirt() that accepts a size and the
text of a message that should be printed on the shirt. The function should print
a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the
function a second time using keyword arguments.
"""

#T-shirt

def make_shirt(size_shirt, message):
    """Displays information about size and text of a message."""
    print(f"I want a {size_shirt}.")
    print(f"I want to see '{message}' written on my {size_shirt.title()}. ")

make_shirt('small shirt', 'Im loving python') 
make_shirt(size_shirt = 'small shirt', message = 'Im loving python')