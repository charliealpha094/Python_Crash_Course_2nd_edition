#Done by Carlos Amaral in 28/06/2020

"""
Write a function called favorite_book() that accepts one
parameter, title . The function should print a message, such as One of my
favorite books is Alice in Wonderland . Call the function, making sure to
include a book title as an argument in the function call.
"""

#Favourite book
def favourite_book(title):
    """Display a favourite book"""
    print(f"One of my favourite books is {title.title()} from George Orwell!")

favourite_book('1984')
