#Done by Carlos Amaral in 03/08/2020

"""
Make a list or tuple containing a series of 10 numbers and
five letters. Randomly select four numbers or letters from the list and print a
message saying that any ticket matching these four numbers or letters wins a
prize.
"""

from random import choice

tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

selected_tickets = []

print("The selected tickets are: ")

while len(selected_tickets) < 4:
    choosed_ticket = choice(tickets)

    if choosed_ticket not in selected_tickets:
        print(f"We pulled a {choosed_ticket}.")
        selected_tickets.append(choosed_ticket)


