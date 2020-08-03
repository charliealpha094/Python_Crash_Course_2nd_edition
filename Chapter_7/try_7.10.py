#Done by Carlos Amaral in 27/06/2020

"""
Write a program that polls users about their dream vaca-
tion. Write a prompt similar to If you could visit one place in the world, where
would you go? Include a block of code that prints the results of the poll.
"""

#Dream vacation

#Define an empty dictionary
responses = {}

#Set a flag to indicate that polling is active
polling_active = True

while polling_active:
    #prompt person's name and response
    name = input("What is your name? ")
    response = input("\nIf you could visit one place in the world," +
                     "where would you go? ")

    #Store the response in the dictionary
    responses[name] = response


    #Find if anyone else is going to take the poll
    repeat = input("Would you like to let anyone else to respond?(yes/no) ")
    if repeat == 'no':
        polling_active = False


#Let's show polling results
print("\n --- Polling Result ---")
for name, response in responses.items():
    print(f"{name} would like to visit {response}.")



