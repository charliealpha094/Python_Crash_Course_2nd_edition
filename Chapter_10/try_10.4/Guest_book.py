#Done by Carlos Amaral in 11/07/2020

"""
Write a while loop that prompts users for their name. When
they enter their name, print a greeting to the screen and add a line recording
their visit in a file called guest_book.txt. Make sure each entry appears on a
new line in the file.
"""

#Guest book

responses = {}

loop_active = True

while loop_active:
    name = input("What is your name? ")
    response = print("Welcome to our event!")

    responses[name] = response


    repeat = input("Would you like to let anyone else to respond? (yes/no)")

    if repeat == 'no':
        loop_active = False



filename = 'guest_book.txt'

with open(filename, 'w') as file:
    for response in responses:
        file.write(f"\n{response} has been in our event!")