#Done by Carlos Amaral in 15/06/2020

"""
Think of at least three kinds of your favorite pizza. Store these
pizza names in a list, and then use a for loop to print the name of each pizza.
• Modify your for loop to print a sentence using the name of the pizza
instead of printing just the name of the pizza. For each pizza you should
have one line of output containing a simple statement like I like pepperoni
pizza.
• Add a line at the end of your program, outside the for loop, that states
how much you like pizza. The output should consist of three or more lines
about the kinds of pizza you like and then an additional sentence, such as
I really love pizza!
"""

pizzas = ['papperoni', 'neapolitan', 'margheritta', 'carbonara']
for pizza in pizzas:
	print(pizza)

print("\n")

for pizza in pizzas:
    print(f"I really enjoy to eat, {pizza.title()}" + " pizza!")

print("\nI really love pizza")	