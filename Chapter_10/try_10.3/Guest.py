#Done by Carlos Amaral in 11/07/2020

"""
Write a program that prompts the user for their name. When they
respond, write their name to a file called guest.txt.
"""

#Guest


guest = input("Please, enter your name: ")

filename = 'guest.txt'

with open(filename, 'w') as file:
    file.write(f"Name is {guest}")



