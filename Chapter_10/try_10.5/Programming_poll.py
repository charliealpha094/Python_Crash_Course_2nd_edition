#Done by Carlos Amaral in 11/07/2020


#Programming poll

"""
Programming Poll: Write a while loop that asks people why they like
programming. Each time someone enters a reason, add their reason to a file
that stores all the responses.
"""

responses = {}

loop_active = True

while loop_active:
    question = input("Why do you like programming? ")
    response = print("Thanks for our answer!")

    responses[question] = response

    repeat = input("Is anyone else there to respond? (yes/no) ")

    if repeat == 'no':
        loop_active = False

print("Thanks for participating in our poll!")

filename = 'programming_poll.txt'

with open(filename, 'w') as file:
    for response in responses:
        file.write(f"{response}")