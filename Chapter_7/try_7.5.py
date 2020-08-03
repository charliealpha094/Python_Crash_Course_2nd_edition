#Done by Carlos Amaral in 24/06/2020

"""
A movie theater charges different ticket prices depending on
a person’s age. If a person is under the age of 3, the ticket is free; if they are
between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
$15. Write a loop in which you ask users their age, and then tell them the cost
of their movie ticket.
"""

#Movie tickets
prompt = "\nPlease, tell me your age: "
prompt += "\nEnter 'quit' to end the program. "

while True:
    age = input(prompt)

    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("You have a free ticket.")
    if age < 12:
        print("Your ticket price is 10$.")
    if age > 12:
        print("Your ticket price is 15$.")
